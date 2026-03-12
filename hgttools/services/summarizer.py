"""汇总服务 - 按(名称+规格+等级+材质)分组汇总"""

from typing import List, Dict, Tuple
from ..models.material import Part, SummaryItem
from ..data.materials import get_material


class SummaryCalculator:
    """汇总计算器"""

    def summarize(self, parts: List[Part]) -> List[SummaryItem]:
        """
        多条件汇总零件
        按(名称+规格+等级+材质)分组汇总，与VBA sum()逻辑一致

        分组键: (名称, 规格, 等级, 材质)
        累加字段: 设计量(quantity)
        """
        groups: Dict[Tuple, List[Part]] = {}

        # 按汇总键分组
        for part in parts:
            # 分组键：(名称+规格+等级+材质)
            key = (part.name, part.specification, part.grade or "", part.material)
            if key not in groups:
                groups[key] = []
            groups[key].append(part)

        # 生成汇总项
        summary_items = []
        for idx, (key, group_parts) in enumerate(groups.items(), 1):
            name, spec, grade, material = key

            # 计算总量（设计量累加）
            total_quantity = sum(p.quantity for p in group_parts)
            total_weight = sum(p.total_weight for p in group_parts)
            total_surface = sum(p.surface_area for p in group_parts)

            # 从材料库获取材料信息
            # 匹配键：(名称+规格+材质)
            mat = get_material(name, spec, material)

            item = SummaryItem(
                seq_no=idx,
                name=name,
                specification=spec,
                grade=grade,
                design_quantity=total_quantity,
                total_quantity=total_quantity,
                unit=group_parts[0].unit if group_parts else "",
                unit_weight=mat.unit_weight if mat else 0,
                total_weight=total_weight,
                tech_condition=mat.tech_condition if mat else "",
                material=material,
                unit_surface_area=mat.unit_surface_area if mat else 0,
                surface_area=total_surface
            )

            # 如果没有匹配到材料，使用零件的技术条件
            if not item.tech_condition and group_parts:
                item.tech_condition = group_parts[0].tech_condition

            summary_items.append(item)

        # 排序：先按名称，再按材质（与VBA逻辑一致）
        summary_items.sort(key=lambda x: (x.name, x.material))

        # 重新编号
        for idx, item in enumerate(summary_items, 1):
            item.seq_no = idx

        return summary_items

    def add_subtotals(self, items: List[SummaryItem]) -> List[SummaryItem]:
        """
        按材质添加小计行（与VBA subtotal()逻辑一致）

        在汇总表中按材质分组，在每个材质组后插入小计行
        """
        if not items:
            return items

        result = []
        current_material = None
        group_start_idx = 0

        for idx, item in enumerate(items):
            if item.material != current_material and current_material is not None:
                # 插入小计行
                subtotal = self._create_subtotal(result, group_start_idx, len(result), current_material)
                result.append(subtotal)
                group_start_idx = len(result)

            result.append(item)
            current_material = item.material

        # 添加最后一个小计行
        if result:
            subtotal = self._create_subtotal(result, group_start_idx, len(result), current_material)
            result.append(subtotal)

        # 重新编号
        for idx, item in enumerate(result, 1):
            item.seq_no = idx

        return result

    def _create_subtotal(self, items: List[SummaryItem], start_idx: int, end_idx: int, material: str) -> SummaryItem:
        """创建小计行"""
        # 计算小计范围内的总量
        total_qty = sum(items[i].design_quantity for i in range(start_idx, end_idx))
        total_weight = sum(items[i].total_weight for i in range(start_idx, end_idx))

        return SummaryItem(
            seq_no=0,  # 稍后重新编号
            name="小 计",
            specification="",
            grade="",
            design_quantity=total_qty,
            total_quantity=total_qty,
            unit=items[start_idx].unit if start_idx < len(items) else "",
            unit_weight=0,
            total_weight=total_weight,
            tech_condition="",
            material=material
        )
