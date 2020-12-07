#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# tkinter实现菜单功能
# 运行，点击Edit菜单下的Show Image，会显示一张图片，点击Show Text会出现一行文本。
# https://blog.csdn.net/u011541946/article/details/71374512

from tkinter import *
from os import path
from PIL import Image, ImageTk


class App(Frame):
    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("第一个窗体")

        self.pack(fill=BOTH, expand=1)

        # 实例化一个Menu对象，这个在主窗体添加一个菜单
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # 创建File菜单，下面有Save和Exit两个子菜单
        file = Menu(menu)
        file.add_command(label='Save')
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        # 创建Edit菜单，下面有一个Undo菜单
        edit = Menu(menu)
        edit.add_command(label='Undo')
        edit.add_command(label='Show  Image', command=self.showImg)
        edit.add_command(label='Show  Text', command=self.showTxt)
        menu.add_cascade(label='Edit', menu=edit)

    def client_exit(self):
        exit()

    def showImg(self):
        d = path.dirname(__file__)  # 返回当前文件所在的目录
        filename = d + '/image.gif'
        load = Image.open(filename)
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showTxt(self):
        text = Label(self, text='GUI图形编程')
        text.pack()


root = Tk()
root.geometry("400x300")
app = App(root)
root.mainloop()
