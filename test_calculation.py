"""测试修正后的计算逻辑"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from hgttools.services.parser import SupportCodeParser
from hgttools.services.calculator import PartCalculator

def test_d4_calculation():
    """测试D4型号计算"""
    print("=" * 60)
    print("测试D4型号计算")
    print("=" * 60)

    parser = SupportCodeParser()
    calculator = PartCalculator()

    # 测试用例: D4-2-D-1000-200
    # 期望结果:
    # - 槽钢设计量 = 1000 × 2 ÷ 1000 = 2.0 m
    # - 钢板设计量 = 1 × 100 × 200 × 2 ÷ 1000000 = 0.04 m²

    test_code = "D4-2-D-1000-200"
    parsed = parser.parse(test_code)

    print(f"\n输入编号: {test_code}")
    print(f"解析结果:")
    print(f"  - 型号: {parsed.model}")
    print(f"  - 数量: {parsed.extra_params.get('quantity')}")
    print(f"  - 子项: {parsed.sub_item}")
    print(f"  - 长度: {parsed.length} mm")
    print(f"  - 筋板高度: {parsed.height} mm")

    parts = calculator.calculate(parsed, quantity=1, seq_no=1)

    print(f"\n计算结果:")
    for part in parts:
        print(f"  - {part.name} {part.specification}: {part.quantity} {part.unit}")

    # 验证结果
    assert len(parts) == 2, f"期望2个零件，实际{len(parts)}个"
    assert abs(parts[0].quantity - 2.0) < 0.001, f"槽钢设计量应为2.0，实际{parts[0].quantity}"
    assert abs(parts[1].quantity - 0.04) < 0.001, f"钢板设计量应为0.04，实际{parts[1].quantity}"

    print("\n✓ D4测试通过!")
    return True

def test_u1_calculation():
    """测试U1型号计算"""
    print("\n" + "=" * 60)
    print("测试U1型号计算")
    print("=" * 60)

    parser = SupportCodeParser()
    calculator = PartCalculator()

    # 测试用例: U1-A-200-C1, 数量=2
    # 期望结果:
    # - U型螺栓: 2套
    # - 角钢∠50x6: 0.3 × 2 = 0.6 m

    test_code = "U1-A-200-C1"
    parsed = parser.parse(test_code)

    print(f"\n输入编号: {test_code}")
    print(f"解析结果:")
    print(f"  - 型号: {parsed.model}")
    print(f"  - 类型: {parsed.support_type}")
    print(f"  - 管径: {parsed.pipe_diameter}")
    print(f"  - 材质代码: {parsed.material_code}")

    parts = calculator.calculate(parsed, quantity=2, seq_no=1)

    print(f"\n计算结果 (数量=2):")
    for part in parts:
        print(f"  - {part.name} {part.specification}: {part.quantity} {part.unit}")

    # 验证结果
    assert len(parts) == 2, f"期望2个零件，实际{len(parts)}个"

    # 找到U型螺栓和角钢
    u_bolt = next((p for p in parts if p.name == "U型螺栓"), None)
    angle_steel = next((p for p in parts if p.name == "角钢"), None)

    assert u_bolt is not None, "未找到U型螺栓"
    assert angle_steel is not None, "未找到角钢"

    assert abs(u_bolt.quantity - 2.0) < 0.001, f"U型螺栓数量应为2.0，实际{u_bolt.quantity}"
    assert abs(angle_steel.quantity - 0.6) < 0.001, f"角钢数量应为0.6，实际{angle_steel.quantity}"

    print("\n✓ U1测试通过!")
    return True

def test_d4_with_external_quantity():
    """测试D4型号带外部数量的计算"""
    print("\n" + "=" * 60)
    print("测试D4型号带外部数量的计算")
    print("=" * 60)

    parser = SupportCodeParser()
    calculator = PartCalculator()

    # 测试用例: D4-2-D-1000-200, 输入表格数量=3
    # 期望结果:
    # - 槽钢设计量 = 1000 × 2 × 3 ÷ 1000 = 6.0 m
    # - 钢板设计量 = 1 × 100 × 200 × 2 × 3 ÷ 1000000 = 0.12 m²

    test_code = "D4-2-D-1000-200"
    parsed = parser.parse(test_code)

    print(f"\n输入编号: {test_code}, 外部数量=3")

    parts = calculator.calculate(parsed, quantity=3, seq_no=1)

    print(f"\n计算结果:")
    for part in parts:
        print(f"  - {part.name} {part.specification}: {part.quantity} {part.unit}")

    # 验证结果
    assert abs(parts[0].quantity - 6.0) < 0.001, f"槽钢设计量应为6.0，实际{parts[0].quantity}"
    assert abs(parts[1].quantity - 0.12) < 0.001, f"钢板设计量应为0.12，实际{parts[1].quantity}"

    print("\n✓ D4带外部数量测试通过!")
    return True

if __name__ == "__main__":
    try:
        test_d4_calculation()
        test_u1_calculation()
        test_d4_with_external_quantity()
        print("\n" + "=" * 60)
        print("所有测试通过!")
        print("=" * 60)
    except AssertionError as e:
        print(f"\n✗ 测试失败: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ 测试出错: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
