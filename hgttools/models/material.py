"""材料和零件数据模型"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Material:
    """材料定义"""
    name: str                      # 名称及编码
    specification: str             # 规格
    grade: Optional[str] = None    # 等级
    unit: str = ""                 # 单位
    unit_weight: float = 0.0       # 单重(Kg)
    tech_condition: str = ""       # 技术条件
    material_type: str = ""        # 材质
    unit_surface_area: float = 0.0 # 单位表面积 m/m²

    def calculate_weight(self, quantity: float) -> float:
        """计算总重"""
        return self.unit_weight * quantity

    def calculate_surface_area(self, quantity: float) -> float:
        """计算表面积"""
        return self.unit_surface_area * quantity


@dataclass
class Part:
    """零件"""
    # 基础信息
    seq_no: int = 0                # 序号
    support_code: str = ""         # 管架编号
    support_seq: int = 0           # 管架序号

    # 零件信息
    name: str = ""                 # 名称
    specification: str = ""        # 规格
    grade: Optional[str] = None    # 等级
    quantity: float = 0.0          # 数量/设计量
    unit: str = ""                 # 单位
    material: str = ""             # 材质
    unit_weight: float = 0.0       # 单重
    total_weight: float = 0.0      # 总重
    tech_condition: str = ""       # 技术条件
    remark: str = ""               # 备注
    unit_surface_area: float = 0.0 # 单位表面积
    surface_area: float = 0.0      # 零件面积

    def calculate(self, material_db: dict):
        """根据材料库计算重量"""
        key = (self.name, self.specification, self.material)
        if key in material_db:
            mat = material_db[key]
            self.unit_weight = mat.unit_weight
            self.total_weight = self.unit_weight * self.quantity
            self.tech_condition = mat.tech_condition
            self.unit_surface_area = mat.unit_surface_area
            self.surface_area = self.unit_surface_area * self.quantity


@dataclass
class SummaryItem:
    """汇总项"""
    seq_no: int = 0                # 序号
    name: str = ""                 # 名称及编码
    specification: str = ""        # 规格
    grade: Optional[str] = None    # 等级
    design_quantity: float = 0.0   # 设计量
    margin: float = 0.0            # 设计裕量
    total_quantity: float = 0.0    # 总量
    unit: str = ""                 # 单位
    unit_weight: float = 0.0       # 单重(Kg)
    total_weight: float = 0.0      # 总重(Kg)
    tech_condition: str = ""       # 技术条件
    remark: str = ""               # 备注
    material: str = ""             # 材质
    unit_surface_area: float = 0.0 # 单位表面积
    surface_area: float = 0.0      # 零件面积

    @property
    def summary_key(self) -> tuple:
        """汇总键 - 用于多条件分组"""
        return (self.name, self.specification, self.grade or "", self.material)
