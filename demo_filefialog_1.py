#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 选择文件弹窗

from tkinter import *
from tkinter.filedialog import *

root = Tk()

fd = FileDialog(root)  # 创建打开文件对话框
filename = fd.go()  # 显示打开文件对话框，并获取选择的文件名称
print(filename)

root.mainloop()
