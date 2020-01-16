"""
安装Pillow:
pip install Pillow

为避免用pip一个一个安装，还需要考虑兼容性，建议安装anaconda:https://www.anaconda.com/
安装后file->settings->Project Interpreter->设置按钮add->Existing environment->选择anaconda下的python.exe
"""
# 打印Python解释器搜索路径
import sys

import numpy

path = sys.path
print(path)
