"""管架型号数据库 - 从HGT21629管架标准图输入和计算书提取

每个型号的结构：
{
    "model": "型号代码",
    "drawing_no": "施工图号",
    "parts": [
        {
            "sub_item": "子项代码",
            "name": "零件名称",
            "spec": "规格",
            "unit": "单位",
            "material": "材质",
            "pipe_diameter": 公称直径(可选),
            "outer_diameter": 外径(可选),
            ...其他参数
        }
    ]
}
"""

from typing import Dict, List, Any, Optional


# 管架型号数据库
SUPPORTS_DB: Dict[str, Dict[str, Any]] = {
    # ========== A1型号 - U型螺栓 ==========
    "A1": {
        "model": "A1",
        "drawing_no": "图C.1-1",
        "name": "U型螺栓",
        "unit": "套",
        "materials": {
            "C1": "Q235B",
            "S": "06Cr19Ni10",
            "S1": "Q235B+EPDM",
        },
        "parts": [
            {"name": "U型螺栓", "spec_template": "DN{pipe_diameter}", "unit": "套", "material_code": "{material_code}"}
        ]
    },

    # ========== U1型号 - U型螺栓（另一种） ==========
    "U1": {
        "model": "U1",
        "drawing_no": "图C.19-1",
        "name": "U型螺栓",
        "unit": "套",
        "materials": {
            "C1": "Q235B",
            "S": "06Cr19Ni10",
            "S1": "Q235B+EPDM",
        },
        "parts": [
            {"name": "U型螺栓", "spec_template": "DN{pipe_diameter}", "unit": "套", "material_code": "{material_code}"}
        ]
    },

    # ========== D4型号 - 吊架 ==========
    "D4": {
        "model": "D4",
        "drawing_no": "图C.4-4",
        "description": "吊架",
        "sub_items": {
            "A": {
                "name": "角钢",
                "spec": "∠50x6",
                "unit": "m",
                "material": "Q235B",
                # 无筋板
            },
            "B": {
                "name": "角钢",
                "spec": "∠75x7",
                "unit": "m",
                "material": "Q235B",
                # 无筋板
            },
            "C": {
                "name": "角钢",
                "spec": "∠100x10",
                "unit": "m",
                "material": "Q235B",
                "plate": {
                    "name": "钢板",
                    "spec": "δ=10",
                    "unit": "m²",
                    "material": "Q235B",
                    "width": 100,  # 筋板宽度(mm)
                    "qty_type": 1  # 数量类型：1=2块
                }
            },
            "D": {
                "name": "槽钢",
                "spec": "[12.6",
                "unit": "m",
                "material": "Q235B",
                "plate": {
                    "name": "钢板",
                    "spec": "δ=10",
                    "unit": "m²",
                    "material": "Q235B",
                    "width": 100,  # 筋板宽度(mm)
                    "qty_type": 2  # 数量类型：2=1块
                }
            },
        }
    },

    # ========== E1型号 - 管卡 ==========
    "E1": {
        "model": "E1",
        "drawing_no": "图C.5-1",
        "description": "管卡",
        "sub_items": {
            "A": {"name": "钢板", "spec": "δ=10", "base_qty": 0.025, "unit": "m²", "material": "Q235B",
                  "stainless": {"name": "钢板", "spec": "δ=1", "size": "50x50", "area": 0.0025, "unit": "m²", "material": "06Cr18Ni9"}},
            "B": {"name": "角钢", "spec": "∠50x6", "unit": "m", "material": "Q235B",
                  "stainless": {"name": "钢板", "spec": "δ=2", "size": "50x60", "area": 0.003, "unit": "m²", "material": "06Cr18Ni9"}},
            "C": {"name": "槽钢", "spec": "[10", "unit": "m", "material": "Q235B",
                  "stainless": {"name": "钢板", "spec": "δ=2", "size": "100x80", "area": 0.008, "unit": "m²", "material": "06Cr18Ni9"}},
            "D": {"name": "H型钢", "spec": "H100x100x6x8", "unit": "m", "material": "Q235B",
                  "stainless": {"name": "钢板", "spec": "δ=2", "size": "100x90", "area": 0.009, "unit": "m²", "material": "06Cr18Ni9"}},
            "E": {"name": "H型钢", "spec": "H150x150x7x10", "unit": "m", "material": "Q235B",
                  "stainless": {"name": "钢板", "spec": "δ=2", "size": "150x100", "area": 0.015, "unit": "m²", "material": "06Cr18Ni9"}},
        },
        "material_codes": {"S": "06Cr18Ni9"}
    },

    # ========== F2型号 - 耳轴支架 ==========
    "F2": {
        "model": "F2",
        "drawing_no": "图C.6-2",
        "description": "耳轴支架",
        "base_parts": {
            "name": "结构用无缝钢管",
            "unit": "m",
            "material": "见材料编码",
        },
        "pipe_data": [
            {"dn": 6, "outer": 10.2},
            {"dn": 8, "outer": 13.5},
            {"dn": 10, "outer": 17.2},
            {"dn": 15, "outer": 21.3},
            {"dn": 20, "outer": 26.9},
            {"dn": 25, "outer": 33.7},
            {"dn": 32, "outer": 42.4},
            {"dn": 40, "outer": 48.3},
            {"dn": 50, "outer": 60.3},
            {"dn": 65, "outer": 76.1},
            {"dn": 80, "outer": 88.9},
            {"dn": 100, "outer": 114.3},
            {"dn": 125, "outer": 139.7},
            {"dn": 150, "outer": 168.3},
            {"dn": 200, "outer": 219.1},
            {"dn": 250, "outer": 273},
            {"dn": 300, "outer": 323.9},
            {"dn": 350, "outer": 355.6},
            {"dn": 400, "outer": 406.4},
            {"dn": 450, "outer": 457},
            {"dn": 500, "outer": 508},
            {"dn": 550, "outer": 559},
            {"dn": 600, "outer": 610},
            {"dn": 650, "outer": 660},
            {"dn": 700, "outer": 711},
            {"dn": 750, "outer": 762},
            {"dn": 800, "outer": 813},
            {"dn": 850, "outer": 864},
            {"dn": 900, "outer": 914},
            {"dn": 950, "outer": 965},
            {"dn": 1000, "outer": 1016},
            {"dn": 1050, "outer": 1067},
            {"dn": 1100, "outer": 1118},
            {"dn": 1150, "outer": 1168},
            {"dn": 1200, "outer": 1219},
        ],
        # 方形底板(A型)
        "square_base": {
            "name": "钢板",
            "spec": "δ=10",  # 根据管径变化
            "material": "Q235B",
        },
        # 圆形底板(B型)
        "round_base": {
            "name": "钢板",
            "spec": "δ=10",
            "material": "Q235B",
        },
        "material_codes": {
            "L": "Q345E",
            "C1": "Q235B",
            "C2": "20",
            "A1": "15CrMoG",
            "A2": "12Cr1MoVG",
            "S": "06Cr19Ni10",
        }
    },

    # ========== Q3型号 - 支撑架 ==========
    "Q3": {
        "model": "Q3",
        "drawing_no": "图C.15-3",
        "description": "支撑架",
        "sub_items": {
            "A": {"name": "角钢", "spec": "∠50x6", "unit": "m", "material": "Q235B"},
            "B": {"name": "角钢", "spec": "∠75x7", "unit": "m", "material": "Q235B"},
            "C": {"name": "角钢", "spec": "∠100x10", "unit": "m", "material": "Q235B"},
        },
        "pipe_data": [
            {"dn": 6, "outer": 10.2},
            {"dn": 8, "outer": 13.5},
            {"dn": 10, "outer": 17.2},
            {"dn": 15, "outer": 21.3},
            {"dn": 20, "outer": 26.9},
            {"dn": 25, "outer": 33.7},
            {"dn": 32, "outer": 42.4},
            {"dn": 40, "outer": 48.3},
            {"dn": 50, "outer": 60.3},
            {"dn": 65, "outer": 76.1},
            {"dn": 80, "outer": 88.9},
            {"dn": 100, "outer": 114.3},
            {"dn": 125, "outer": 139.7},
            {"dn": 150, "outer": 168.3},
            {"dn": 200, "outer": 219.1},
            {"dn": 250, "outer": 273},
            {"dn": 300, "outer": 323.9},
            {"dn": 350, "outer": 355.6},
            {"dn": 400, "outer": 406.4},
            {"dn": 450, "outer": 457},
            {"dn": 500, "outer": 508},
            {"dn": 550, "outer": 559},
            {"dn": 600, "outer": 610},
            {"dn": 650, "outer": 660},
            {"dn": 700, "outer": 711},
            {"dn": 750, "outer": 762},
            {"dn": 800, "outer": 813},
            {"dn": 850, "outer": 864},
            {"dn": 900, "outer": 914},
            {"dn": 950, "outer": 965},
            {"dn": 1000, "outer": 1016},
            {"dn": 1050, "outer": 1067},
            {"dn": 1100, "outer": 1118},
            {"dn": 1150, "outer": 1168},
            {"dn": 1200, "outer": 1219},
        ]
    },

    # ========== D5型号 - 吊架（带筋板） ==========
    "D5": {
        "model": "D5",
        "drawing_no": "图C.4-5",
        "description": "吊架（带筋板高度）",
        # D5有多个子项类型，每个类型有不同的主材和筋板配置
        # 编号格式: D5-数量-子项-类型-长度-筋板高度-垫板尺寸
        "sub_items": {
            "A": {
                "name": "角钢",
                "spec": "∠100x10",
                "unit": "m",
                "material": "Q235B",
                "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2}
            },
            "B": {
                "name": "角钢",
                "spec": "∠125x10",
                "unit": "m",
                "material": "Q235B",
                "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2}
            },
            "C": {
                "name": "H型钢",
                "spec": "H150x150x7x10",
                "unit": "m",
                "material": "Q235B",
                "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2}
            },
            "D": {
                "name": "H型钢",
                "spec": "H250x250x9x14",
                "unit": "m",
                "material": "Q235B",
                "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 60, "qty_type": 2},
                "extra": {"name": "角钢", "spec": "∠200x14", "unit": "m", "material": "Q235B"}
            },
            "E": {
                "name": "H型钢",
                "spec": "H250x250x9x14",
                "unit": "m",
                "material": "Q235B",
                "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2},
                "extra": {"name": "角钢", "spec": "∠200x14", "unit": "m", "material": "Q235B"}
            },
            "F": {
                "name": "H型钢",
                "spec": "H250x250x9x14",
                "unit": "m",
                "material": "Q235B",
                "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2},
                "extra": {"name": "角钢", "spec": "∠200x14", "unit": "m", "material": "Q235B"}
            },
        }
    },

    # ========== D6-D8型号 ==========
    "D6": {
        "model": "D6",
        "drawing_no": "图C.4-6",
        "description": "吊架",
        "sub_items": {
            "A": {"name": "槽钢", "spec": "[10", "unit": "m", "material": "Q235B"},
            "B": {"name": "槽钢", "spec": "[12.6", "unit": "m", "material": "Q235B"},
            "C": {"name": "槽钢", "spec": "[14a", "unit": "m", "material": "Q235B"},
            "D": {"name": "槽钢", "spec": "[25a", "unit": "m", "material": "Q235B"},
            "E": {"name": "槽钢", "spec": "[20a", "unit": "m", "material": "Q235B"},
            "F": {"name": "槽钢", "spec": "[20a", "unit": "m", "material": "Q235B"},
            "G": {"name": "槽钢", "spec": "[20a", "unit": "m", "material": "Q235B"},
        }
    },
    "D7": {
        "model": "D7",
        "drawing_no": "图C.4-7",
        "description": "吊架",
        "sub_items": {
            "A": {"name": "H型钢", "spec": "H100x100x6x8", "unit": "m", "material": "Q235B"},
            "B": {"name": "H型钢", "spec": "H125x125x6.5x9", "unit": "m", "material": "Q235B"},
            "C": {"name": "H型钢", "spec": "H150x150x7x10", "unit": "m", "material": "Q235B"},
            "D": {"name": "H型钢", "spec": "H194x150x6x9", "unit": "m", "material": "Q235B"},
            "E": {"name": "H型钢", "spec": "H125x125x6.5x9", "unit": "m", "material": "Q235B"},
            "F": {"name": "H型钢", "spec": "H194x150x6x9", "unit": "m", "material": "Q235B"},
            "G": {"name": "H型钢", "spec": "H244x175x7x11", "unit": "m", "material": "Q235B"},
        }
    },
    "D8": {
        "model": "D8",
        "drawing_no": "图C.4-8",
        "description": "吊架",
        "sub_items": {
            "A": {"name": "H型钢", "spec": "H200x200x8x12", "unit": "m", "material": "Q235B"},
            "B": {"name": "H型钢", "spec": "H250x250x9x14", "unit": "m", "material": "Q235B"},
            "C": {"name": "H型钢", "spec": "H200x200x8x12", "unit": "m", "material": "Q235B"},
            "D": {"name": "H型钢", "spec": "H250x250x9x14", "unit": "m", "material": "Q235B"},
            "E": {"name": "槽钢", "spec": "[20a", "unit": "m", "material": "Q235B"},
            "F": {"name": "槽钢", "spec": "[28c", "unit": "m", "material": "Q235B"},
        }
    },

    # ========== D9型号 ==========
    "D9": {
        "model": "D9",
        "drawing_no": "图C.4-9",
        "description": "吊架（带垫板）",
        "sub_items": {
            "A": {"name": "H型钢", "spec": "H100x100x6x8", "unit": "m", "material": "Q235B",
                  "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2}},
            "B": {"name": "H型钢", "spec": "H125x125x6.5x9", "unit": "m", "material": "Q235B",
                  "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2}},
            "C": {"name": "H型钢", "spec": "H200x200x8x12", "unit": "m", "material": "Q235B",
                  "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2}},
            "D": {"name": "H型钢", "spec": "H250x250x9x14", "unit": "m", "material": "Q235B",
                  "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2}},
            "E": {"name": "槽钢", "spec": "[20a", "unit": "m", "material": "Q235B",
                  "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2}},
            "F": {"name": "槽钢", "spec": "[28c", "unit": "m", "material": "Q235B",
                  "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2}},
        }
    },

    # ========== D10型号 ==========
    "D10": {
        "model": "D10",
        "drawing_no": "图C.4-10",
        "description": "吊架（组合型）",
        "sub_items": {
            "A": {
                "name": "角钢",
                "spec": "∠50x6",
                "unit": "m",
                "material": "Q235B",
                "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2}
            },
            "A1": {
                "name": "角钢",
                "spec": "∠50x6",
                "unit": "m",
                "material": "Q235B",
                "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2}
            },
        }
    },

    # ========== D11-D14型号 ==========
    "D11": {
        "model": "D11",
        "drawing_no": "图C.4-11",
        "description": "吊架",
        "sub_items": {
            "A": {"name": "H型钢", "spec": "H100x100x6x8", "unit": "m", "material": "Q235B"},
            "B": {"name": "H型钢", "spec": "H100x100x6x8", "unit": "m", "material": "Q235B"},
            "C": {"name": "H型钢", "spec": "H125x125x6.5x9", "unit": "m", "material": "Q235B"},
            "D": {"name": "H型钢", "spec": "H150x150x7x10", "unit": "m", "material": "Q235B"},
        }
    },
    "D12": {
        "model": "D12",
        "drawing_no": "图C.4-12",
        "description": "吊架",
        "sub_items": {
            "A": {"name": "H型钢", "spec": "H250x250x9x14", "unit": "m", "material": "Q235B"},
            "B": {"name": "H型钢", "spec": "H250x250x9x14", "unit": "m", "material": "Q235B"},
            "C": {"name": "H型钢", "spec": "H250x250x9x14", "unit": "m", "material": "Q235B"},
            "G": {"name": "H型钢", "spec": "H250x250x9x14", "unit": "m", "material": "Q235B"},
        }
    },
    "D13": {
        "model": "D13",
        "drawing_no": "图C.4-13",
        "description": "吊架",
        "sub_items": {
            "A": {"name": "H型钢", "spec": "H250x250x9x14", "unit": "m", "material": "Q235B"},
            "B": {"name": "H型钢", "spec": "H250x250x9x14", "unit": "m", "material": "Q235B"},
            "C": {"name": "H型钢", "spec": "H250x250x9x14", "unit": "m", "material": "Q235B"},
            "D": {"name": "H型钢", "spec": "H250x250x9x14", "unit": "m", "material": "Q235B"},
        }
    },
    "D14": {
        "model": "D14",
        "drawing_no": "图C.4-14",
        "description": "吊架",
        "sub_items": {
            "A": {"name": "H型钢", "spec": "H100x100x6x8", "unit": "m", "material": "Q235B",
                  "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 1}},
            "B": {"name": "H型钢", "spec": "H100x100x6x8", "unit": "m", "material": "Q235B",
                  "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 1}},
        }
    },

    # ========== D15-D20型号 ==========
    "D15": {
        "model": "D15",
        "drawing_no": "图C.4-15",
        "description": "吊架",
        "sub_items": {
            "A": {
                "name": "角钢",
                "spec": "∠50x6",
                "unit": "m",
                "material": "Q235B",
                "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2}
            },
        }
    },
    "D16": {
        "model": "D16",
        "drawing_no": "图C.4-16",
        "description": "吊架",
        "sub_items": {
            "A": {
                "name": "槽钢",
                "spec": "[14a",
                "unit": "m",
                "material": "Q235B",
                "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2}
            },
            "B": {
                "name": "槽钢",
                "spec": "[14a",
                "unit": "m",
                "material": "Q235B",
                "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2}
            },
            "C": {
                "name": "槽钢",
                "spec": "[14a",
                "unit": "m",
                "material": "Q235B",
                "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2}
            },
        }
    },
    "D17": {
        "model": "D17",
        "drawing_no": "图C.4-17",
        "description": "吊架",
        "sub_items": {
            "A": {
                "name": "H型钢",
                "spec": "H125x125x6.5x9",
                "unit": "m",
                "material": "Q235B",
                "extra1": {"name": "角钢", "spec": "∠100x10", "unit": "m", "material": "Q235B"},
                "extra2": {"name": "槽钢", "spec": "[8", "unit": "m", "material": "Q235B"}
            },
        }
    },
    "D18": {
        "model": "D18",
        "drawing_no": "图C.4-18",
        "description": "吊架",
        "sub_items": {
            "A": {
                "name": "角钢",
                "spec": "∠50x6",
                "unit": "m",
                "material": "Q235B",
                "plate": {"name": "钢板", "spec": "δ=10", "unit": "m²", "material": "Q235B", "width": 100, "qty_type": 2}
            },
        }
    },
    "D19": {"model": "D19", "drawing_no": "图C.4-19", "description": "吊架"},
    "D20": {"model": "D20", "drawing_no": "图C.4-20", "description": "吊架"},

    # ========== E2-E10型号 ==========
    "E2": {"model": "E2", "drawing_no": "图C.5-2", "description": "管卡"},
    "E3": {"model": "E3", "drawing_no": "图C.5-3", "description": "管卡"},
    "E4": {"model": "E4", "drawing_no": "图C.5-4", "description": "管卡"},
    "E5": {"model": "E5", "drawing_no": "图C.5-5", "description": "管卡"},
    "E6": {"model": "E6", "drawing_no": "图C.5-6", "description": "管卡"},
    "E7": {"model": "E7", "drawing_no": "图C.5-7", "description": "管卡"},
    "E8": {"model": "E8", "drawing_no": "图C.5-8", "description": "管卡"},
    "E9": {"model": "E9", "drawing_no": "图C.5-9", "description": "管卡"},
    "E10": {"model": "E10", "drawing_no": "图C.5-10", "description": "管卡"},

    # ========== F3-F14型号 ==========
    "F3": {"model": "F3", "drawing_no": "图C.6-3", "description": "耳轴支架"},
    "F4": {"model": "F4", "drawing_no": "图C.6-4", "description": "耳轴支架"},
    "F5": {"model": "F5", "drawing_no": "图C.6-5", "description": "耳轴支架"},
    "F6": {"model": "F6", "drawing_no": "图C.6-6", "description": "耳轴支架"},
    "F7": {"model": "F7", "drawing_no": "图C.6-7", "description": "耳轴支架"},
    "F8": {"model": "F8", "drawing_no": "图C.6-8", "description": "耳轴支架"},
    "F9": {"model": "F9", "drawing_no": "图C.6-9", "description": "耳轴支架"},
    "F10": {"model": "F10", "drawing_no": "图C.6-10", "description": "耳轴支架"},
    "F11": {"model": "F11", "drawing_no": "图C.6-11", "description": "耳轴支架"},
    "F12": {"model": "F12", "drawing_no": "图C.6-12", "description": "耳轴支架"},
    "F13": {"model": "F13", "drawing_no": "图C.6-13", "description": "耳轴支架"},
    "F14": {"model": "F14", "drawing_no": "图C.6-14", "description": "耳轴支架"},

    # ========== G1-G17型号 ==========
    "G1": {"model": "G1", "drawing_no": "图C.7-1", "description": "支架"},
    "G2": {"model": "G2", "drawing_no": "图C.7-2", "description": "支架"},
    "G3": {"model": "G3", "drawing_no": "图C.7-3", "description": "支架"},
    "G4": {"model": "G4", "drawing_no": "图C.7-4", "description": "支架"},
    "G5": {"model": "G5", "drawing_no": "图C.7-5", "description": "支架"},
    "G6": {"model": "G6", "drawing_no": "图C.7-6", "description": "支架"},
    "G11": {"model": "G11", "drawing_no": "图C.7-11", "description": "支架"},
    "G12": {"model": "G12", "drawing_no": "图C.7-12", "description": "支架"},
    "G13": {"model": "G13", "drawing_no": "图C.7-13", "description": "支架"},
    "G14": {"model": "G14", "drawing_no": "图C.7-14", "description": "支架"},
    "G15": {"model": "G15", "drawing_no": "图C.7-15", "description": "支架"},
    "G16": {"model": "G16", "drawing_no": "图C.7-16", "description": "支架"},
    "G17": {"model": "G17", "drawing_no": "图C.7-17", "description": "支架"},

    # ========== H1-H2型号 ==========
    "H1": {"model": "H1", "drawing_no": "图C.8-1", "description": "支架"},
    "H2": {"model": "H2", "drawing_no": "图C.8-2", "description": "支架"},

    # ========== J1-J13型号 ==========
    "J1": {"model": "J1", "drawing_no": "图C.10-1", "description": "支架"},
    "J2": {"model": "J2", "drawing_no": "图C.10-2", "description": "支架"},
    "J13": {"model": "J13", "drawing_no": "图C.10-13", "description": "支架"},

    # ========== K1-K2型号 ==========
    "K1": {"model": "K1", "drawing_no": "图C.11-1", "description": "支架"},
    "K2": {"model": "K2", "drawing_no": "图C.11-2", "description": "支架"},

    # ========== Q1-Q7型号 ==========
    "Q1": {"model": "Q1", "drawing_no": "图C.15-1", "description": "支撑架"},
    "Q2": {"model": "Q2", "drawing_no": "图C.15-2", "description": "支撑架"},
    "Q4": {"model": "Q4", "drawing_no": "图C.15-4", "description": "支撑架"},
    "Q5": {"model": "Q5", "drawing_no": "图C.15-5", "description": "支撑架"},
    "Q6": {"model": "Q6", "drawing_no": "图C.15-6", "description": "支撑架"},
    "Q7": {"model": "Q7", "drawing_no": "图C.15-7", "description": "支撑架"},

    # ========== U2-U6型号 ==========
    "U2": {"model": "U2", "drawing_no": "图C.19-2", "description": "U型螺栓"},
    "U3": {"model": "U3", "drawing_no": "图C.19-3", "description": "U型螺栓"},
    "U4": {"model": "U4", "drawing_no": "图C.19-4", "description": "U型螺栓"},
    "U5": {"model": "U5", "drawing_no": "图C.19-5", "description": "U型螺栓"},
    "U6": {"model": "U6", "drawing_no": "图C.19-6", "description": "U型螺栓"},

    # ========== Y1-Y4型号 ==========
    "Y1": {"model": "Y1", "drawing_no": "图C.21-1", "description": "支架"},
    "Y2": {"model": "Y2", "drawing_no": "图C.21-2", "description": "支架"},
    "Y4": {"model": "Y4", "drawing_no": "图C.21-4", "description": "支架"},
}


def get_support_model(model: str) -> Optional[Dict[str, Any]]:
    """获取管架型号定义"""
    return SUPPORTS_DB.get(model.upper())


def list_models() -> List[str]:
    """列出所有支持的型号"""
    return sorted(SUPPORTS_DB.keys())
