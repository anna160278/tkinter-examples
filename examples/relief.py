#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# relief属性

from tkinter import *
from tkinter import ttk

RELIEF = ["flat", "raised", "sunken", "solid", "ridge", "groove"]

root = Tk()
root.title("relief演示")
for i in range(len(RELIEF)):
    temp = ttk.Frame(
        root, relief=RELIEF[i], borderwidth=5, width=50, height=50)
    label = ttk.Label(temp, text=RELIEF[i])
    label.grid(row=0, column=0)
    temp.grid(row=1, column=i, padx=10, pady=10)

root.mainloop()
