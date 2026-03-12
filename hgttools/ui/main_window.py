"""GUI主窗口"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from typing import List, Tuple
import os

from ..services.parser import SupportCodeParser
from ..services.calculator import PartCalculator
from ..services.summarizer import SummaryCalculator
from ..services.exporter import ExcelExporter
from ..models.pipe_support import PipeSupportCode
from ..models.material import Part, SummaryItem


class MainWindow:
    """主窗口类"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("HGT21629管架标准图汇料工具 v1.0")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 600)

        # 初始化服务
        self.parser = SupportCodeParser()
        self.calculator = PartCalculator()
        self.summary_calc = SummaryCalculator()
        self.exporter = ExcelExporter()

        # 数据存储
        self.input_data: List[Tuple[str, int]] = []  # (管架编号, 数量)
        self.parts: List[Part] = []
        self.summary_items: List[SummaryItem] = []

        # 创建界面
        self._create_menu()
        self._create_input_section()
        self._create_button_section()
        self._create_result_section()
        self._create_status_bar()

    def _create_menu(self):
        """创建菜单栏"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # 文件菜单
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="文件", menu=file_menu)
        file_menu.add_command(label="导入Excel/CSV...", command=self._import_file)
        file_menu.add_separator()
        file_menu.add_command(label="导出BOM...", command=self._export_bom)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.root.quit)

        # 操作菜单
        action_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="操作", menu=action_menu)
        action_menu.add_command(label="添加行", command=self._add_row)
        action_menu.add_command(label="删除选中行", command=self._delete_selected)
        action_menu.add_separator()
        action_menu.add_command(label="计算", command=self._calculate)
        action_menu.add_command(label="清空", command=self._clear_all)

        # 帮助菜单
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="帮助", menu=help_menu)
        help_menu.add_command(label="使用说明", command=self._show_help)
        help_menu.add_command(label="关于", command=self._show_about)

    def _create_input_section(self):
        """创建输入区域"""
        # 输入区框架
        input_frame = ttk.LabelFrame(self.root, text="管架编号输入", padding=10)
        input_frame.pack(fill=tk.X, padx=10, pady=5)

        # 工具栏
        toolbar = ttk.Frame(input_frame)
        toolbar.pack(fill=tk.X, pady=(0, 5))

        ttk.Button(toolbar, text="添加行", command=self._add_row).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="删除选中", command=self._delete_selected).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="导入...", command=self._import_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="清空", command=self._clear_all).pack(side=tk.LEFT, padx=2)

        # 创建表格
        columns = ("序号", "管架编号", "数量", "状态")
        self.input_tree = ttk.Treeview(input_frame, columns=columns, show='headings', height=8)

        # 设置列
        self.input_tree.heading("序号", text="序号")
        self.input_tree.heading("管架编号", text="管架编号")
        self.input_tree.heading("数量", text="数量")
        self.input_tree.heading("状态", text="状态")

        self.input_tree.column("序号", width=60, anchor="center")
        self.input_tree.column("管架编号", width=200)
        self.input_tree.column("数量", width=80, anchor="center")
        self.input_tree.column("状态", width=80, anchor="center")

        # 滚动条
        scrollbar = ttk.Scrollbar(input_frame, orient=tk.VERTICAL, command=self.input_tree.yview)
        self.input_tree.configure(yscrollcommand=scrollbar.set)

        self.input_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 绑定双击编辑
        self.input_tree.bind('<Double-1>', self._on_input_double_click)

        # 添加一些示例数据
        self._add_row_values("Q3-4-A-200-25-1024-500", 1)
        self._add_row_values("U1-A-200-C1", 1)
        self._add_row_values("D4-2-D-1000-200", 1)

    def _create_button_section(self):
        """创建按钮区域"""
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)

        # 主要操作按钮
        ttk.Button(btn_frame, text="计算", command=self._calculate, width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="导出BOM", command=self._export_bom, width=15).pack(side=tk.LEFT, padx=5)

        # 右侧帮助信息
        help_text = "提示: 双击表格可直接编辑，回车确认"
        ttk.Label(btn_frame, text=help_text, foreground="gray").pack(side=tk.RIGHT, padx=5)

    def _create_result_section(self):
        """创建结果展示区域"""
        # 使用Notebook创建标签页
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # 汇总表标签页
        self.summary_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.summary_frame, text="汇总表")
        self._create_summary_tree()

        # 零件明细表标签页
        self.parts_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.parts_frame, text="零件明细表")
        self._create_parts_tree()

    def _create_summary_tree(self):
        """创建汇总表Treeview"""
        columns = ("序号", "名称及编码", "规格", "等级", "设计量", "总量", "单位",
                   "单重", "总重", "技术条件", "材质", "单位表面积", "零件面积")

        self.summary_tree = ttk.Treeview(self.summary_frame, columns=columns, show='headings')

        # 设置列标题
        for col in columns:
            self.summary_tree.heading(col, text=col)

        # 设置列宽
        widths = {
            "序号": 50, "名称及编码": 150, "规格": 100, "等级": 60,
            "设计量": 70, "总量": 70, "单位": 50, "单重": 80,
            "总重": 80, "技术条件": 200, "材质": 80, "单位表面积": 100, "零件面积": 80
        }
        for col, width in widths.items():
            self.summary_tree.column(col, width=width, anchor="center" if col in ["序号", "单位"] else "w")

        # 滚动条
        vsb = ttk.Scrollbar(self.summary_frame, orient=tk.VERTICAL, command=self.summary_tree.yview)
        hsb = ttk.Scrollbar(self.summary_frame, orient=tk.HORIZONTAL, command=self.summary_tree.xview)
        self.summary_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # 布局
        self.summary_tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')

        self.summary_frame.grid_rowconfigure(0, weight=1)
        self.summary_frame.grid_columnconfigure(0, weight=1)

    def _create_parts_tree(self):
        """创建零件明细表Treeview"""
        columns = ("序号", "管架编号", "名称", "规格", "数量", "单位",
                   "材质", "单重", "总重", "技术条件", "单位表面积", "零件面积")

        self.parts_tree = ttk.Treeview(self.parts_frame, columns=columns, show='headings')

        # 设置列标题
        for col in columns:
            self.parts_tree.heading(col, text=col)

        # 设置列宽
        widths = {
            "序号": 50, "管架编号": 150, "名称": 120, "规格": 100,
            "数量": 70, "单位": 50, "材质": 80, "单重": 80,
            "总重": 80, "技术条件": 200, "单位表面积": 100, "零件面积": 80
        }
        for col, width in widths.items():
            self.parts_tree.column(col, width=width, anchor="center" if col in ["序号", "单位"] else "w")

        # 滚动条
        vsb = ttk.Scrollbar(self.parts_frame, orient=tk.VERTICAL, command=self.parts_tree.yview)
        hsb = ttk.Scrollbar(self.parts_frame, orient=tk.HORIZONTAL, command=self.parts_tree.xview)
        self.parts_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # 布局
        self.parts_tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')

        self.parts_frame.grid_rowconfigure(0, weight=1)
        self.parts_frame.grid_columnconfigure(0, weight=1)

    def _create_status_bar(self):
        """创建状态栏"""
        self.status_bar = ttk.Label(self.root, text="就绪", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=2)

    def _set_status(self, message: str):
        """设置状态栏消息"""
        self.status_bar.config(text=message)
        self.root.update_idletasks()

    def _add_row(self):
        """添加新行"""
        self._add_row_values("", 1)

    def _add_row_values(self, code: str, qty: int):
        """添加带值的行"""
        seq = len(self.input_tree.get_children()) + 1
        status = "有效" if code and self.parser.parse(code) else "待输入"
        self.input_tree.insert('', tk.END, values=(seq, code, qty, status))

    def _delete_selected(self):
        """删除选中的行"""
        selected = self.input_tree.selection()
        if not selected:
            messagebox.showwarning("警告", "请先选择要删除的行")
            return

        for item in selected:
            self.input_tree.delete(item)

        # 重新编号
        self._renumber_input_rows()

    def _renumber_input_rows(self):
        """重新编号输入行"""
        for idx, item in enumerate(self.input_tree.get_children(), 1):
            values = list(self.input_tree.item(item, 'values'))
            values[0] = idx
            self.input_tree.item(item, values=values)

    def _on_input_double_click(self, event):
        """处理输入表双击事件"""
        item = self.input_tree.identify('item', event.x, event.y)
        column = self.input_tree.identify_column(event.x)

        if not item:
            return

        # 获取当前值
        values = list(self.input_tree.item(item, 'values'))
        col_idx = int(column[1:]) - 1  # #1 -> 0

        if col_idx not in [1, 2]:  # 只允许编辑管架编号和数量列
            return

        # 创建编辑框
        bbox = self.input_tree.bbox(item, column)
        if not bbox:
            return

        x, y, width, height = bbox

        entry = ttk.Entry(self.input_tree, width=width)
        entry.place(x=x, y=y, width=width, height=height)
        entry.insert(0, values[col_idx])
        entry.select_range(0, tk.END)
        entry.focus()

        def on_return(event):
            new_value = entry.get()
            values[col_idx] = new_value

            # 如果编辑的是管架编号，验证并更新状态
            if col_idx == 1:
                parsed = self.parser.parse(new_value)
                values[3] = "有效" if parsed else "无效"

            # 如果编辑的是数量，确保是数字
            if col_idx == 2:
                try:
                    values[2] = int(new_value)
                except ValueError:
                    values[2] = 1

            self.input_tree.item(item, values=values)
            entry.destroy()

        def on_escape(event):
            entry.destroy()

        entry.bind('<Return>', on_return)
        entry.bind('<Escape>', on_escape)
        entry.bind('<FocusOut>', lambda e: entry.destroy())

    def _get_input_data(self) -> List[Tuple[str, int]]:
        """获取输入数据"""
        data = []
        for item in self.input_tree.get_children():
            values = self.input_tree.item(item, 'values')
            code = str(values[1]).strip()
            try:
                qty = int(values[2])
            except (ValueError, IndexError):
                qty = 1
            if code:
                data.append((code, qty))
        return data

    def _calculate(self):
        """执行计算"""
        self._set_status("正在计算...")

        # 获取输入数据
        self.input_data = self._get_input_data()

        if not self.input_data:
            messagebox.showwarning("警告", "请输入至少一个管架编号")
            self._set_status("就绪")
            return

        # 解析和计算
        self.parts = []
        errors = []

        for seq_no, (code, qty) in enumerate(self.input_data, 1):
            parsed = self.parser.parse(code)
            if not parsed:
                errors.append(f"第{seq_no}行: 无法解析 '{code}'")
                continue

            parts = self.calculator.calculate(parsed, qty, seq_no)
            self.parts.extend(parts)

        if errors:
            error_msg = "\n".join(errors[:10])
            if len(errors) > 10:
                error_msg += f"\n...还有{len(errors)-10}个错误"
            messagebox.showerror("解析错误", error_msg)
            self._set_status("计算完成，但有错误")
        else:
            self._set_status("计算成功")

        # 汇总
        self.summary_items = self.summary_calc.summarize(self.parts)

        # 更新显示
        self._update_summary_display()
        self._update_parts_display()

        self._set_status(f"计算完成: {len(self.input_data)}个管架, {len(self.parts)}个零件, {len(self.summary_items)}个汇总项")

    def _update_summary_display(self):
        """更新汇总表显示"""
        # 清空
        for item in self.summary_tree.get_children():
            self.summary_tree.delete(item)

        # 填充数据
        for item in self.summary_items:
            self.summary_tree.insert('', tk.END, values=(
                item.seq_no,
                item.name,
                item.specification,
                item.grade or "",
                f"{item.design_quantity:.4f}",
                f"{item.total_quantity:.4f}",
                item.unit,
                f"{item.unit_weight:.4f}",
                f"{item.total_weight:.4f}",
                item.tech_condition,
                item.material,
                f"{item.unit_surface_area:.4f}",
                f"{item.surface_area:.4f}"
            ))

    def _update_parts_display(self):
        """更新零件明细表显示"""
        # 清空
        for item in self.parts_tree.get_children():
            self.parts_tree.delete(item)

        # 填充数据
        for part in self.parts:
            self.parts_tree.insert('', tk.END, values=(
                part.seq_no,
                part.support_code,
                part.name,
                part.specification,
                f"{part.quantity:.4f}",
                part.unit,
                part.material,
                f"{part.unit_weight:.4f}",
                f"{part.total_weight:.4f}",
                part.tech_condition,
                f"{part.unit_surface_area:.4f}",
                f"{part.surface_area:.4f}"
            ))

    def _export_bom(self):
        """导出BOM清单"""
        if not self.summary_items:
            messagebox.showwarning("警告", "请先执行计算")
            return

        # 选择保存路径
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel文件", "*.xlsx"), ("所有文件", "*.*")],
            title="导出BOM清单"
        )

        if not file_path:
            return

        try:
            self._set_status("正在导出...")

            # 生成单支架零件表（去重后）
            single_parts = self._generate_single_support_parts()

            # 导出
            self.exporter.export(self.parts, self.summary_items, single_parts, file_path)

            self._set_status(f"已导出到: {file_path}")
            messagebox.showinfo("成功", f"BOM清单已导出到:\n{file_path}")

        except Exception as e:
            messagebox.showerror("导出失败", str(e))
            self._set_status("导出失败")

    def _generate_single_support_parts(self) -> List[Part]:
        """生成单支架零件表（去重）"""
        seen = set()
        result = []
        seq = 1

        for part in self.parts:
            key = (part.support_code, part.name, part.specification)
            if key not in seen:
                seen.add(key)
                new_part = Part(
                    seq_no=seq,
                    support_code=part.support_code,
                    name=part.name,
                    specification=part.specification,
                    quantity=part.quantity,
                    unit=part.unit,
                    material=part.material,
                    unit_weight=part.unit_weight,
                    total_weight=part.total_weight,
                    tech_condition=part.tech_condition,
                    unit_surface_area=part.unit_surface_area,
                    surface_area=part.surface_area
                )
                result.append(new_part)
                seq += 1

        return result

    def _import_file(self):
        """从文件导入管架列表"""
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Excel文件", "*.xlsx *.xls"),
                ("CSV文件", "*.csv"),
                ("文本文件", "*.txt"),
                ("所有文件", "*.*")
            ],
            title="导入管架列表"
        )

        if not file_path:
            return

        try:
            self._set_status("正在导入...")

            if file_path.endswith('.csv'):
                import csv
                with open(file_path, 'r', encoding='utf-8-sig') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if len(row) >= 2:
                            self._add_row_values(row[0], int(row[1]) if row[1].isdigit() else 1)
                        elif len(row) == 1:
                            self._add_row_values(row[0], 1)

            elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                import pandas as pd
                df = pd.read_excel(file_path)
                for _, row in df.iterrows():
                    code = str(row.iloc[0]) if pd.notna(row.iloc[0]) else ""
                    qty = int(row.iloc[1]) if len(row) > 1 and pd.notna(row.iloc[1]) else 1
                    if code:
                        self._add_row_values(code, qty)

            else:
                # 文本文件，每行一个编号
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        code = line.strip()
                        if code:
                            self._add_row_values(code, 1)

            self._renumber_input_rows()
            self._set_status(f"导入完成: {file_path}")

        except Exception as e:
            messagebox.showerror("导入失败", str(e))
            self._set_status("导入失败")

    def _clear_all(self):
        """清空所有数据"""
        if messagebox.askyesno("确认", "确定要清空所有数据吗？"):
            # 清空输入
            for item in self.input_tree.get_children():
                self.input_tree.delete(item)

            # 清空结果
            for item in self.summary_tree.get_children():
                self.summary_tree.delete(item)
            for item in self.parts_tree.get_children():
                self.parts_tree.delete(item)

            # 重置数据
            self.input_data = []
            self.parts = []
            self.summary_items = []

            self._set_status("已清空")

    def _show_help(self):
        """显示帮助"""
        help_text = """
HGT21629管架标准图汇料工具 使用说明

1. 输入管架编号
   - 在输入表格中双击可直接编辑
   - 支持批量导入Excel/CSV/文本文件

2. 管架编号格式示例:
   - A1-200-C1 (U型螺栓)
   - D4-2-D-1000-200 (吊架)
   - F2-100-50-C1-500-C-F-UP-HE (耳轴支架)
   - Q3-4-A-200-25-1024-500 (支撑架)

3. 执行计算
   - 点击"计算"按钮或选择操作菜单
   - 计算结果将显示在"汇总表"和"零件明细表"中

4. 导出BOM
   - 计算完成后点击"导出BOM"
   - 选择保存路径，生成Excel文件

5. 注意事项
   - 确保管架编号格式正确
   - 数量必须为整数
   - 导出前请先执行计算
"""
        messagebox.showinfo("使用说明", help_text)

    def _show_about(self):
        """显示关于对话框"""
        about_text = """
HGT21629管架标准图汇料工具 v1.0

基于HGT21629管架标准图开发
用于管架材料统计和BOM生成

技术栈:
- Python 3.x
- tkinter (GUI)
- openpyxl (Excel处理)

功能:
- 管架编号解析
- 零件自动拆分
- 材料汇总统计
- Excel BOM导出
"""
        messagebox.showinfo("关于", about_text)

    def run(self):
        """运行主循环"""
        self.root.mainloop()


def main():
    """主入口"""
    app = MainWindow()
    app.run()


if __name__ == "__main__":
    main()
