"""管架数据模型"""

from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List


@dataclass
class PipeSupportCode:
    """管架编号解析结果"""
    raw_code: str                      # 原始编号
    model: str                         # 型号 (A1, D4, F2, Q3等)
    sub_item: Optional[str] = None     # 子项 (A, B, C等)
    support_type: Optional[str] = None # 类型
    pipe_diameter: Optional[int] = None    # 管径 (DN)
    pipe_diameter2: Optional[int] = None   # 被支撑管径 (用于Q3等)
    length: Optional[int] = None       # 长度
    height: Optional[int] = None       # 高度/筋板高度
    material_code: Optional[str] = None    # 材质代码
    material: Optional[str] = None     # 材质
    extra_params: Dict[str, Any] = field(default_factory=dict)  # 其他参数

    def __str__(self):
        return f"{self.model}(子项={self.sub_item}, 管径={self.pipe_diameter})"


@dataclass
class PipeSupport:
    """管架实例"""
    code: PipeSupportCode      # 解析后的编号
    quantity: int = 1          # 数量
    parts: List['Part'] = field(default_factory=list)  # 零件列表

    def __str__(self):
        return f"{self.code.raw_code} x {self.quantity}"
