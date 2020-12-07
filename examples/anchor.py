# -*- coding: utf-8 -*-
# Tkinter位置anchor

'''首先介绍对齐方式。Tkinter小部件的对齐方式用属性anchor。
anchor取值有tk.N（上），tk.NE（右上），tk.E（右），tk.SE（右下），tk.S（下），tk.SW（左下），tk.W（左），tk.NW（左上），tk.CENTER（中间）。'''

import tkinter as tk
root = tk.Tk()
for a in [tk.N, tk.NE, tk.E, tk.SE, tk.S, tk.SW, tk.W, tk.NW, tk.CENTER]:
    f = tk.Frame(root, borderwidth=2, bg='#ddd', height=20, width=20)
    tk.Label(f, text=str(a), fg='black', anchor=a, height=5, width=10).pack()
    f.pack(side=tk.LEFT)
root.mainloop()
