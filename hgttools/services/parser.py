"""管架编号解析服务"""

import re
from typing import Optional
from ..models.pipe_support import PipeSupportCode


class SupportCodeParser:
    """管架编号解析器"""

    # 型号列表
    MODELS = ['A1', 'A2', 'A3', 'A4', 'A5',
              'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10',
              'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20',
              'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10',
              'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10',
              'F11', 'F12', 'F13', 'F14',
              'G1', 'G2', 'G3', 'G4', 'G5', 'G6',
              'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17',
              'H1', 'H2',
              'J1', 'J2', 'J13',
              'K1', 'K2',
              'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7',
              'U1', 'U2', 'U3', 'U4', 'U5', 'U6',
              'Y1', 'Y2', 'Y4']

    def parse(self, code: str) -> Optional[PipeSupportCode]:
        """
        解析管架编号

        格式：型号-参数1-参数2-...
        不同型号有不同的参数格式
        """
        if not code or not isinstance(code, str):
            return None

        code = code.strip()
        if not code:
            return None

        # 提取型号（编号的开头部分）
        model = self._extract_model(code)
        if not model:
            return None

        # 根据型号调用对应的解析器
        parser_method = getattr(self, f'_parse_{model.lower()}', self._parse_generic)
        return parser_method(code, model)

    def _extract_model(self, code: str) -> Optional[str]:
        """从编号中提取型号"""
        # 按优先级排序，先匹配较长的型号（如D10在D1之前）
        for model in sorted(self.MODELS, key=len, reverse=True):
            if code.upper().startswith(model + '-'):
                return model
            if code.upper() == model:
                return model
        return None

    def _parse_generic(self, code: str, model: str) -> PipeSupportCode:
        """通用解析器"""
        parts = code.split('-')
        return PipeSupportCode(
            raw_code=code,
            model=model,
            extra_params={'parts': parts}
        )

    def _parse_a1(self, code: str, model: str) -> PipeSupportCode:
        """解析A1型号: A1-管径-材质代码"""
        # 格式: A1-200-C1 或 A1-200
        parts = code.split('-')

        pipe_diameter = None
        material_code = None

        if len(parts) >= 2:
            try:
                pipe_diameter = int(parts[1])
            except ValueError:
                pass

        if len(parts) >= 3:
            material_code = parts[2]

        return PipeSupportCode(
            raw_code=code,
            model=model,
            pipe_diameter=pipe_diameter,
            material_code=material_code,
            material=self._get_material_name(material_code)
        )

    def _parse_u1(self, code: str, model: str) -> PipeSupportCode:
        """解析U1型号: U1-类型-管径-材质代码"""
        # 格式: U1-A-200-C1
        parts = code.split('-')

        support_type = None
        pipe_diameter = None
        material_code = None

        if len(parts) >= 2:
            support_type = parts[1]  # A, B等

        if len(parts) >= 3:
            try:
                pipe_diameter = int(parts[2])
            except ValueError:
                pass

        if len(parts) >= 4:
            material_code = parts[3]

        return PipeSupportCode(
            raw_code=code,
            model=model,
            support_type=support_type,
            pipe_diameter=pipe_diameter,
            material_code=material_code,
            material=self._get_material_name(material_code)
        )

    def _parse_d4(self, code: str, model: str) -> PipeSupportCode:
        """
        解析D4型号: D4-数量-子项-长度-筋板高度

        格式: D4-2-D-1000-200
        - 2: 数量
        - D: 子项 (A, B, C, D)
        - 1000: 长度(mm)
        - 200: 筋板高度(mm)
        """
        parts = code.split('-')

        quantity = 1  # 默认数量
        sub_item = None
        length = None
        height = None

        if len(parts) >= 2:
            try:
                quantity = int(parts[1])  # 数量
            except ValueError:
                quantity = 1

        if len(parts) >= 3:
            sub_item = parts[2]  # A, B, C, D等

        if len(parts) >= 4:
            try:
                length = int(parts[3])  # 长度(mm)
            except ValueError:
                pass

        if len(parts) >= 5:
            try:
                height = int(parts[4])  # 筋板高度(mm)
            except ValueError:
                pass

        return PipeSupportCode(
            raw_code=code,
            model=model,
            sub_item=sub_item,
            length=length,
            height=height,
            extra_params={'quantity': quantity}  # 数量存入extra_params
        )

    def _parse_d5(self, code: str, model: str) -> PipeSupportCode:
        """
        解析D5型号: D5-数量-子项-筋板高度-长度-垫板尺寸
        格式: D5-2-D-1000-1150-200x300
        """
        parts = code.split('-')

        quantity = 1
        sub_item = None
        length = None
        height = None
        plate_size = None

        if len(parts) >= 2:
            try:
                quantity = int(parts[1])  # 数量
            except ValueError:
                quantity = 1

        if len(parts) >= 3:
            sub_item = parts[2]  # A, B, C, D, E, F

        # 根据测试数据分析，parts[3]是筋板高度，parts[4]是长度
        if len(parts) >= 4:
            try:
                height = int(parts[3])  # 筋板高度(mm)
            except ValueError:
                pass

        if len(parts) >= 5:
            try:
                length = int(parts[4])  # 长度(mm)
            except ValueError:
                pass

        if len(parts) >= 6:
            plate_size = parts[5]  # 200x300格式

        return PipeSupportCode(
            raw_code=code,
            model=model,
            sub_item=sub_item,
            length=length,
            height=height,
            extra_params={'quantity': quantity, 'plate_size': plate_size}
        )

    def _parse_d6(self, code: str, model: str) -> PipeSupportCode:
        """解析D6型号: D6-数量-子项-长度-高度"""
        # 格式: D6-1-D-600-750
        return self._parse_d4(code, model)

    def _parse_d7(self, code: str, model: str) -> PipeSupportCode:
        """解析D7型号: D7-数量-子项-长度-高度"""
        return self._parse_d4(code, model)

    def _parse_d8(self, code: str, model: str) -> PipeSupportCode:
        """解析D8型号: D8-数量-子项-长度-高度"""
        return self._parse_d4(code, model)

    def _parse_d9(self, code: str, model: str) -> PipeSupportCode:
        """
        解析D9型号: D9-类型-长度-高度-垫板尺寸
        格式: D9-E-1000-800-200x300 (无数量字段，数量默认为1)
        """
        parts = code.split('-')

        quantity = 1  # D9无数量字段，默认为1
        support_type = None
        length = None
        height = None
        plate_size = None

        if len(parts) >= 2:
            support_type = parts[1]  # A, B, C, D, E, F

        if len(parts) >= 3:
            try:
                length = int(parts[2])  # 长度(mm)
            except ValueError:
                pass

        if len(parts) >= 4:
            try:
                height = int(parts[3])  # 高度(mm)
            except ValueError:
                pass

        if len(parts) >= 5:
            plate_size = parts[4]  # 200x300格式

        return PipeSupportCode(
            raw_code=code,
            model=model,
            support_type=support_type,
            length=length,
            height=height,
            extra_params={'quantity': quantity, 'plate_size': plate_size}
        )

    def _parse_d10(self, code: str, model: str) -> PipeSupportCode:
        """
        解析D10型号: D10-数量-子项-类型-长度-高度-垫板尺寸
        格式: D10-1-A1-A-1000-800-200x300
        """
        parts = code.split('-')

        quantity = 1
        sub_item = None
        support_type = None
        length = None
        height = None
        plate_size = None

        if len(parts) >= 2:
            try:
                quantity = int(parts[1])  # 数量
            except ValueError:
                quantity = 1

        if len(parts) >= 3:
            sub_item = parts[2]  # A1, A2等子项

        if len(parts) >= 4:
            support_type = parts[3]  # 类型 A, B等

        if len(parts) >= 5:
            try:
                length = int(parts[4])  # 长度(mm)
            except ValueError:
                pass

        if len(parts) >= 6:
            try:
                height = int(parts[5])  # 高度(mm)
            except ValueError:
                pass

        if len(parts) >= 7:
            plate_size = parts[6]  # 200x300格式

        return PipeSupportCode(
            raw_code=code,
            model=model,
            sub_item=sub_item,
            support_type=support_type,
            length=length,
            height=height,
            extra_params={'quantity': quantity, 'plate_size': plate_size}
        )

    def _parse_d11(self, code: str, model: str) -> PipeSupportCode:
        """
        解析D11型号: D11-数量-子项-长度-高度
        格式: D11-1-A-1000-800
        """
        return self._parse_d4(code, model)

    def _parse_d12(self, code: str, model: str) -> PipeSupportCode:
        """
        解析D12型号: D12-数量-子项-长度-高度
        格式: D12-1-A-1000-800
        """
        return self._parse_d4(code, model)

    def _parse_d13(self, code: str, model: str) -> PipeSupportCode:
        """
        解析D13型号: D13-数量-子项-长度-高度
        格式: D13-1-A-1000-800
        """
        return self._parse_d4(code, model)

    def _parse_d14(self, code: str, model: str) -> PipeSupportCode:
        """
        解析D14型号: D14-类型-长度-高度-垫板尺寸
        格式: D14-A-1000-800-200x300 (无数量字段，数量默认为1)
        """
        parts = code.split('-')

        quantity = 1  # D14无数量字段，默认为1
        support_type = None
        length = None
        height = None
        plate_size = None

        if len(parts) >= 2:
            support_type = parts[1]  # A, B

        if len(parts) >= 3:
            try:
                length = int(parts[2])  # 长度(mm)
            except ValueError:
                pass

        if len(parts) >= 4:
            try:
                height = int(parts[3])  # 高度(mm)
            except ValueError:
                pass

        if len(parts) >= 5:
            plate_size = parts[4]  # 200x300格式

        return PipeSupportCode(
            raw_code=code,
            model=model,
            support_type=support_type,
            length=length,
            height=height,
            extra_params={'quantity': quantity, 'plate_size': plate_size}
        )

    def _parse_d15(self, code: str, model: str) -> PipeSupportCode:
        """
        解析D15型号: D15-数量-子项-类型-长度-高度-垫板尺寸
        格式: D15-1-A-A-1000-800-200x300
        """
        return self._parse_d10(code, model)

    def _parse_d16(self, code: str, model: str) -> PipeSupportCode:
        """
        解析D16型号: D16-数量-子项-类型-长度-高度-垫板尺寸
        格式: D16-1-A-A-1000-800-200x300
        """
        return self._parse_d10(code, model)

    def _parse_d17(self, code: str, model: str) -> PipeSupportCode:
        """
        解析D17型号: D17-数量-子项-长度1-高度1-长度2-高度2
        格式: D17-2-A-1000-800-600-500 (注意：无类型字段)
        """
        parts = code.split('-')

        quantity = 1
        sub_item = None
        length = None
        height = None
        length2 = None
        height2 = None

        if len(parts) >= 2:
            try:
                quantity = int(parts[1])  # 数量
            except ValueError:
                quantity = 1

        if len(parts) >= 3:
            sub_item = parts[2]  # 子项

        # D17格式: D17-数量-子项-长度1-高度1-长度2-高度2
        if len(parts) >= 4:
            try:
                length = int(parts[3])  # 长度1(mm)
            except ValueError:
                pass

        if len(parts) >= 5:
            try:
                height = int(parts[4])  # 高度1(mm)
            except ValueError:
                pass

        if len(parts) >= 6:
            try:
                length2 = int(parts[5])  # 长度2(mm)
            except ValueError:
                pass

        if len(parts) >= 7:
            try:
                height2 = int(parts[6])  # 高度2(mm)
            except ValueError:
                pass

        return PipeSupportCode(
            raw_code=code,
            model=model,
            sub_item=sub_item,
            length=length,
            height=height,
            extra_params={'quantity': quantity, 'length2': length2, 'height2': height2}
        )

    def _parse_d16(self, code: str, model: str) -> PipeSupportCode:
        """
        解析D16型号: D16-数量-子项-类型-长度1-高度1-长度2-高度2-垫板尺寸
        格式: D16-2-C-A-1000-800-600-600-200x300
        """
        parts = code.split('-')

        quantity = 1
        sub_item = None
        support_type = None
        length = None
        height = None
        length2 = None
        height2 = None
        plate_size = None

        if len(parts) >= 2:
            try:
                quantity = int(parts[1])  # 数量
            except ValueError:
                quantity = 1

        if len(parts) >= 3:
            sub_item = parts[2]  # 子项

        if len(parts) >= 4:
            support_type = parts[3]  # 类型

        if len(parts) >= 5:
            try:
                length = int(parts[4])  # 长度1(mm)
            except ValueError:
                pass

        if len(parts) >= 6:
            try:
                height = int(parts[5])  # 高度1(mm)
            except ValueError:
                pass

        if len(parts) >= 7:
            try:
                length2 = int(parts[6])  # 长度2(mm)
            except ValueError:
                pass

        if len(parts) >= 8:
            try:
                height2 = int(parts[7])  # 高度2(mm)
            except ValueError:
                pass

        if len(parts) >= 9:
            plate_size = parts[8]  # 200x300格式

        return PipeSupportCode(
            raw_code=code,
            model=model,
            sub_item=sub_item,
            support_type=support_type,
            length=length,
            height=height,
            extra_params={
                'quantity': quantity,
                'length2': length2,
                'height2': height2,
                'plate_size': plate_size
            }
        )

    def _parse_d18(self, code: str, model: str) -> PipeSupportCode:
        """
        解析D18型号: D18-类型-长度-高度-垫板尺寸 (注意：无数量字段)
        格式: D18-A-500-200x301
        """
        parts = code.split('-')

        quantity = 1  # D18无数量字段，默认为1
        support_type = None
        length = None
        height = None
        plate_size = None

        if len(parts) >= 2:
            support_type = parts[1]  # A, B等

        if len(parts) >= 3:
            try:
                length = int(parts[2])  # 长度(mm)
            except ValueError:
                pass

        if len(parts) >= 4:
            # 可能是高度-垫板尺寸组合(如"200x301")或单独的高度
            part3 = parts[3]
            if 'x' in part3:
                # 格式如 "200x301"，表示高度x垫板尺寸
                try:
                    height = int(part3.split('x')[0])
                    plate_size = part3
                except ValueError:
                    plate_size = part3
            else:
                # 尝试解析为高度
                try:
                    height = int(part3)
                    # 如果成功，再检查是否有垫板尺寸
                    if len(parts) >= 5:
                        plate_size = parts[4]
                except ValueError:
                    # 不是高度，可能是垫板尺寸
                    plate_size = part3

        return PipeSupportCode(
            raw_code=code,
            model=model,
            support_type=support_type,
            length=length,
            height=height,
            extra_params={'quantity': quantity, 'plate_size': plate_size}
        )

    def _parse_e1(self, code: str, model: str) -> PipeSupportCode:
        """解析E1型号: E1-类型-管径-材质代码"""
        # 格式: E1-A-200-S
        parts = code.split('-')

        support_type = None
        pipe_diameter = None
        material_code = None

        if len(parts) >= 2:
            support_type = parts[1]

        if len(parts) >= 3:
            try:
                pipe_diameter = int(parts[2])
            except ValueError:
                pass

        if len(parts) >= 4:
            material_code = parts[3]

        return PipeSupportCode(
            raw_code=code,
            model=model,
            support_type=support_type,
            pipe_diameter=pipe_diameter,
            material_code=material_code,
            material=self._get_material_name(material_code)
        )

    def _parse_e2(self, code: str, model: str) -> PipeSupportCode:
        """解析E2型号: E2-类型"""
        parts = code.split('-')

        support_type = None

        if len(parts) >= 2:
            support_type = parts[1]

        return PipeSupportCode(
            raw_code=code,
            model=model,
            support_type=support_type
        )

    def _parse_e3(self, code: str, model: str) -> PipeSupportCode:
        """解析E3型号: E3-类型-长度"""
        parts = code.split('-')

        support_type = None
        length = None

        if len(parts) >= 2:
            support_type = parts[1]

        if len(parts) >= 3:
            try:
                length = int(parts[2])
            except ValueError:
                pass

        return PipeSupportCode(
            raw_code=code,
            model=model,
            support_type=support_type,
            length=length
        )

    def _parse_f2(self, code: str, model: str) -> PipeSupportCode:
        """解析F2型号: F2-支撑管径-被支撑管径-材质代码-长度-底板类型-方向-配件"""
        # 格式: F2-100-50-C1-500-C-F-UP-HE
        parts = code.split('-')

        pipe_diameter = None  # 支撑管径
        pipe_diameter2 = None  # 被支撑管径
        material_code = None
        length = None
        base_type = None  # 底板类型: A方形, B圆形, C无底板
        direction = None  # 方向
        accessory = None  # 配件

        if len(parts) >= 2:
            try:
                pipe_diameter = int(parts[1])
            except ValueError:
                pass

        if len(parts) >= 3:
            try:
                pipe_diameter2 = int(parts[2])
            except ValueError:
                pass

        if len(parts) >= 4:
            material_code = parts[3]

        if len(parts) >= 5:
            try:
                length = int(parts[4])
            except ValueError:
                pass

        if len(parts) >= 6:
            base_type = parts[5]  # A, B, C

        if len(parts) >= 7:
            direction = parts[6]

        if len(parts) >= 8:
            accessory = parts[7]

        return PipeSupportCode(
            raw_code=code,
            model=model,
            pipe_diameter=pipe_diameter,
            pipe_diameter2=pipe_diameter2,
            material_code=material_code,
            material=self._get_material_name(material_code),
            length=length,
            support_type=base_type,
            extra_params={
                'direction': direction,
                'accessory': accessory
            }
        )

    def _parse_f3(self, code: str, model: str) -> PipeSupportCode:
        """解析F3型号"""
        return self._parse_f2(code, model)

    def _parse_f4(self, code: str, model: str) -> PipeSupportCode:
        """解析F4型号"""
        return self._parse_f2(code, model)

    def _parse_f5(self, code: str, model: str) -> PipeSupportCode:
        """解析F5型号"""
        return self._parse_f2(code, model)

    def _parse_f6(self, code: str, model: str) -> PipeSupportCode:
        """解析F6型号"""
        return self._parse_f2(code, model)

    def _parse_f7(self, code: str, model: str) -> PipeSupportCode:
        """解析F7型号"""
        return self._parse_f2(code, model)

    def _parse_f8(self, code: str, model: str) -> PipeSupportCode:
        """解析F8型号"""
        return self._parse_f2(code, model)

    def _parse_f9(self, code: str, model: str) -> PipeSupportCode:
        """解析F9型号"""
        return self._parse_f2(code, model)

    def _parse_q3(self, code: str, model: str) -> PipeSupportCode:
        """解析Q3型号: Q3-类型-子项-支撑管径-被支撑管径-高度-长度"""
        # 格式: Q3-4-A-200-25-1024-500
        parts = code.split('-')

        support_type = None  # 类型编号
        sub_item = None  # 子项
        pipe_diameter = None  # 支撑管径
        pipe_diameter2 = None  # 被支撑管径
        height = None
        length = None

        if len(parts) >= 2:
            support_type = parts[1]

        if len(parts) >= 3:
            sub_item = parts[2]

        if len(parts) >= 4:
            try:
                pipe_diameter = int(parts[3])
            except ValueError:
                pass

        if len(parts) >= 5:
            try:
                pipe_diameter2 = int(parts[4])
            except ValueError:
                pass

        if len(parts) >= 6:
            try:
                height = int(parts[5])
            except ValueError:
                pass

        if len(parts) >= 7:
            try:
                length = int(parts[6])
            except ValueError:
                pass

        return PipeSupportCode(
            raw_code=code,
            model=model,
            support_type=support_type,
            sub_item=sub_item,
            pipe_diameter=pipe_diameter,
            pipe_diameter2=pipe_diameter2,
            height=height,
            length=length
        )

    def _parse_g1(self, code: str, model: str) -> PipeSupportCode:
        """解析G1型号: G1-类型"""
        parts = code.split('-')

        support_type = None

        if len(parts) >= 2:
            support_type = parts[1]

        return PipeSupportCode(
            raw_code=code,
            model=model,
            support_type=support_type
        )

    def _parse_g2(self, code: str, model: str) -> PipeSupportCode:
        """解析G2型号: G2-子项-类型-管径"""
        parts = code.split('-')

        sub_item = None
        support_type = None
        pipe_diameter = None

        if len(parts) >= 2:
            sub_item = parts[1]

        if len(parts) >= 3:
            support_type = parts[2]

        if len(parts) >= 4:
            try:
                pipe_diameter = int(parts[3])
            except ValueError:
                pass

        return PipeSupportCode(
            raw_code=code,
            model=model,
            sub_item=sub_item,
            support_type=support_type,
            pipe_diameter=pipe_diameter
        )

    def _parse_g3(self, code: str, model: str) -> PipeSupportCode:
        """解析G3型号: G3-子项-类型-管径"""
        return self._parse_g2(code, model)

    def _parse_g4(self, code: str, model: str) -> PipeSupportCode:
        """解析G4型号: G4-类型-长度-高度"""
        parts = code.split('-')

        support_type = None
        length = None
        height = None

        if len(parts) >= 2:
            support_type = parts[1]

        if len(parts) >= 3:
            try:
                length = int(parts[2])
            except ValueError:
                pass

        if len(parts) >= 4:
            try:
                height = int(parts[3])
            except ValueError:
                pass

        return PipeSupportCode(
            raw_code=code,
            model=model,
            support_type=support_type,
            length=length,
            height=height
        )

    def _parse_g5(self, code: str, model: str) -> PipeSupportCode:
        """解析G5型号"""
        return self._parse_g4(code, model)

    def _parse_g6(self, code: str, model: str) -> PipeSupportCode:
        """解析G6型号"""
        return self._parse_g4(code, model)

    def _parse_h1(self, code: str, model: str) -> PipeSupportCode:
        """解析H1型号: H1-子项-类型-管径-被支撑管径-方向"""
        parts = code.split('-')

        sub_item = None
        support_type = None
        pipe_diameter = None
        pipe_diameter2 = None
        direction = None

        if len(parts) >= 2:
            sub_item = parts[1]

        if len(parts) >= 3:
            support_type = parts[2]

        if len(parts) >= 4:
            try:
                pipe_diameter = int(parts[3])
            except ValueError:
                pass

        if len(parts) >= 5:
            try:
                pipe_diameter2 = int(parts[4])
            except ValueError:
                pass

        if len(parts) >= 6:
            direction = parts[5]

        return PipeSupportCode(
            raw_code=code,
            model=model,
            sub_item=sub_item,
            support_type=support_type,
            pipe_diameter=pipe_diameter,
            pipe_diameter2=pipe_diameter2,
            extra_params={'direction': direction}
        )

    def _parse_h2(self, code: str, model: str) -> PipeSupportCode:
        """解析H2型号: H2-类型-管径-方向"""
        parts = code.split('-')

        support_type = None
        pipe_diameter = None
        direction = None

        if len(parts) >= 2:
            support_type = parts[1]

        if len(parts) >= 3:
            try:
                pipe_diameter = int(parts[2])
            except ValueError:
                pass

        if len(parts) >= 4:
            direction = parts[3]

        return PipeSupportCode(
            raw_code=code,
            model=model,
            support_type=support_type,
            pipe_diameter=pipe_diameter,
            extra_params={'direction': direction}
        )

    def _parse_j1(self, code: str, model: str) -> PipeSupportCode:
        """解析J1型号: J1-子项-管径-高度-材质代码-方向"""
        parts = code.split('-')

        sub_item = None
        pipe_diameter = None
        height = None
        material_code = None
        direction = None

        if len(parts) >= 2:
            sub_item = parts[1]

        if len(parts) >= 3:
            try:
                pipe_diameter = int(parts[2])
            except ValueError:
                pass

        if len(parts) >= 4:
            try:
                height = int(parts[3])
            except ValueError:
                pass

        if len(parts) >= 5:
            material_code = parts[4]

        if len(parts) >= 6:
            direction = parts[5]

        return PipeSupportCode(
            raw_code=code,
            model=model,
            sub_item=sub_item,
            pipe_diameter=pipe_diameter,
            height=height,
            material_code=material_code,
            material=self._get_material_name(material_code),
            extra_params={'direction': direction}
        )

    def _parse_j2(self, code: str, model: str) -> PipeSupportCode:
        """解析J2型号"""
        return self._parse_j1(code, model)

    def _parse_j13(self, code: str, model: str) -> PipeSupportCode:
        """解析J13型号"""
        return self._parse_j1(code, model)

    def _parse_k1(self, code: str, model: str) -> PipeSupportCode:
        """解析K1型号: K1-类型-被支撑管径-垫板尺寸"""
        parts = code.split('-')

        support_type = None
        pipe_diameter2 = None
        plate_size = None

        if len(parts) >= 2:
            support_type = parts[1]

        if len(parts) >= 3:
            try:
                pipe_diameter2 = int(parts[2])
            except ValueError:
                pass

        if len(parts) >= 4:
            plate_size = parts[3]

        return PipeSupportCode(
            raw_code=code,
            model=model,
            support_type=support_type,
            pipe_diameter2=pipe_diameter2,
            extra_params={'plate_size': plate_size}
        )

    def _parse_k2(self, code: str, model: str) -> PipeSupportCode:
        """解析K2型号: K2-类型-垫板尺寸"""
        parts = code.split('-')

        support_type = None
        plate_size = None

        if len(parts) >= 2:
            support_type = parts[1]

        if len(parts) >= 3:
            plate_size = parts[2]

        return PipeSupportCode(
            raw_code=code,
            model=model,
            support_type=support_type,
            extra_params={'plate_size': plate_size}
        )

    def _get_material_name(self, code: Optional[str]) -> Optional[str]:
        """根据材质代码获取材质名称"""
        from ..data.materials import MATERIAL_CODE_MAP
        if code:
            return MATERIAL_CODE_MAP.get(code, code)
        return None
