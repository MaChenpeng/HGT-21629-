#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HGT21629管架标准图汇料工具 - 启动脚本

使用方法:
    python run.py

或者:
    python -m hgttools
"""

import sys
import os

# 确保可以导入hgttools包
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from hgttools.ui.main_window import main

if __name__ == "__main__":
    main()
