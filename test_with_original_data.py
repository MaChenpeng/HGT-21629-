"""
使用原始计算表数据作为测试
对比Python计算结果与query_table_sample.csv中的期望结果
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import csv
from hgttools.services.parser import SupportCodeParser
from hgttools.services.calculator import PartCalculator
from hgttools.services.summarizer import SummaryCalculator

def load_query_table_sample():
    """加载query_table_sample.csv作为测试数据"""
    test_cases = []

    with open('query_table_sample.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 跳过空行
            if not row.get('管架编号') or row['管架编号'] == '':
                continue

            test_cases.append({
                'code': row['管架编号'],
                'quantity': float(row['数量']) if row['数量'] else 1.0,
                'name': row['名称及编码'],
                'spec': row['规格'],
                'design_qty': float(row['设计量']) if row['设计量'] else 0,
                'unit': row['单位'],
                'material': row['材质']
            })

    return test_cases

def test_with_query_table():
    """使用query_table_sample.csv测试"""
    print("=" * 70)
    print("Testing with query_table_sample.csv data")
    print("=" * 70)

    parser = SupportCodeParser()
    calculator = PartCalculator()

    test_cases = load_query_table_sample()

    print(f"\nLoaded {len(test_cases)} test cases")
    print()

    passed = 0
    failed = 0

    # 按管架编号分组测试
    grouped = {}
    for case in test_cases:
        code = case['code']
        if code not in grouped:
            grouped[code] = []
        grouped[code].append(case)

    for code, expected_parts in grouped.items():
        print(f"Testing: {code}")

        parsed = parser.parse(code)
        if not parsed:
            print(f"  ERROR: Failed to parse {code}")
            failed += 1
            continue

        # 根据型号决定是否使用CSV数量
        # D4/D5等型号的编号中数量已经是总数量，不需要再乘CSV数量
        # D12/D15/D17等型号的编号中数量是单件数量，需要乘CSV数量
        csv_quantity = expected_parts[0]['quantity']
        code_model = parsed.model.upper() if parsed else ""

        # 这些型号的编号中数量是单件数量，需要乘以CSV数量
        # 注意：D17和D18需要特殊处理，因为它们的编号格式不同
        # Q3和U1也需要乘以CSV数量
        models_needing_csv_qty = ['D6', 'D7', 'D8', 'D9', 'D10', 'D12', 'D13', 'D14', 'D15', 'D16', 'D18', 'Q3', 'U1']
        if code_model in models_needing_csv_qty:
            calc_quantity = csv_quantity
        else:
            calc_quantity = 1

        calculated_parts = calculator.calculate(parsed, quantity=calc_quantity, seq_no=1)

        for expected in expected_parts:
            # 查找匹配的零件
            matched = None
            for part in calculated_parts:
                if part.name == expected['name'] and part.specification == expected['spec']:
                    matched = part
                    break

            if matched:
                qty_match = abs(matched.quantity - expected['design_qty']) < 0.01
                if qty_match:
                    unit_safe = matched.unit.replace('²', '2')
                    print(f"  OK: {expected['name']} {expected['spec']}: {matched.quantity} {unit_safe}")
                    passed += 1
                else:
                    unit_safe = expected['unit'].replace('²', '2')
                    actual_unit_safe = matched.unit.replace('²', '2')
                    print(f"  FAIL: {expected['name']} {expected['spec']}")
                    print(f"    Expected: {expected['design_qty']} {unit_safe}")
                    print(f"    Actual:   {matched.quantity} {actual_unit_safe}")
                    failed += 1
            else:
                print(f"  FAIL: Part not found - {expected['name']} {expected['spec']}")
                failed += 1

        print()

    print("=" * 70)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 70)

    return failed == 0

def test_d4_detailed():
    """详细测试D4型号"""
    print("\n" + "=" * 70)
    print("Detailed D4 Test")
    print("=" * 70)

    parser = SupportCodeParser()
    calculator = PartCalculator()

    # 测试D4-2-D-1000-200
    test_code = "D4-2-D-1000-200"
    print(f"\nTest case: {test_code}")
    print("Expected from query_table_sample.csv:")
    print("  - Cao Gang [12.6: 2.0 m")
    print("  - Gang Ban delta=10: 0.04 m2")

    parsed = parser.parse(test_code)
    print(f"\nParsed:")
    print(f"  - model: {parsed.model}")
    print(f"  - quantity: {parsed.extra_params.get('quantity')}")
    print(f"  - sub_item: {parsed.sub_item}")
    print(f"  - length: {parsed.length}")
    print(f"  - height: {parsed.height}")

    parts = calculator.calculate(parsed, quantity=1, seq_no=1)

    print(f"\nCalculated parts:")
    for i, part in enumerate(parts, 1):
        unit_safe = part.unit.replace('²', '2')
        print(f"  {i}. {part.name} {part.specification}: {part.quantity:.4f} {unit_safe}")

    # Verify
    assert len(parts) == 2, f"Expected 2 parts, got {len(parts)}"

    # Check 槽钢
    main_part = parts[0]
    assert main_part.name == "槽钢", f"Expected 槽钢, got {main_part.name}"
    assert main_part.specification == "[12.6", f"Expected [12.6, got {main_part.specification}"
    assert abs(main_part.quantity - 2.0) < 0.001, f"Expected 2.0, got {main_part.quantity}"

    # Check 钢板
    plate_part = parts[1]
    assert plate_part.name == "钢板", f"Expected 钢板, got {plate_part.name}"
    assert plate_part.specification == "δ=10", f"Expected δ=10, got {plate_part.specification}"
    assert abs(plate_part.quantity - 0.04) < 0.001, f"Expected 0.04, got {plate_part.quantity}"

    print("\nAll D4 assertions passed!")
    return True

def test_u1_detailed():
    """详细测试U1型号"""
    print("\n" + "=" * 70)
    print("Detailed U1 Test")
    print("=" * 70)

    parser = SupportCodeParser()
    calculator = PartCalculator()

    # 测试U1-A-200-C1
    test_code = "U1-A-200-C1"
    quantity = 2

    print(f"\nTest case: {test_code}, quantity={quantity}")
    print("Expected:")
    print("  - U-Bolt A1-200-C1: 2.0 set")
    print("  - Angle Steel 50x6: 0.6 m (0.3 * 2)")

    parsed = parser.parse(test_code)
    print(f"\nParsed:")
    print(f"  - model: {parsed.model}")
    print(f"  - support_type: {parsed.support_type}")
    print(f"  - pipe_diameter: {parsed.pipe_diameter}")
    print(f"  - material_code: {parsed.material_code}")

    parts = calculator.calculate(parsed, quantity=quantity, seq_no=1)

    print(f"\nCalculated parts:")
    for i, part in enumerate(parts, 1):
        unit_safe = part.unit.replace('²', '2')
        print(f"  {i}. {part.name} {part.specification}: {part.quantity:.4f} {unit_safe}")

    # Verify
    assert len(parts) == 2, f"Expected 2 parts, got {len(parts)}"

    # Check U型螺栓
    u_bolt = next((p for p in parts if "U型螺栓" in p.name), None)
    assert u_bolt is not None, "U型螺栓 not found"
    assert abs(u_bolt.quantity - 2.0) < 0.001, f"Expected 2.0, got {u_bolt.quantity}"

    # Check 角钢
    angle = next((p for p in parts if "角钢" in p.name), None)
    assert angle is not None, "角钢 not found"
    assert abs(angle.quantity - 0.6) < 0.001, f"Expected 0.6, got {angle.quantity}"

    print("\nAll U1 assertions passed!")
    return True

if __name__ == "__main__":
    try:
        success = True
        success = test_d4_detailed() and success
        success = test_u1_detailed() and success
        success = test_with_query_table() and success

        print("\n" + "=" * 70)
        if success:
            print("ALL TESTS PASSED!")
        else:
            print("SOME TESTS FAILED!")
        print("=" * 70)

        sys.exit(0 if success else 1)

    except Exception as e:
        print(f"\nTest error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
