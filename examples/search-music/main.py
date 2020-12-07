#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter
import tkinter.messagebox

import search

root = tkinter.Tk()  # 创建窗口对象的背景色

# mp3 = search.searchMusic(searchInputKey)

# 搜索框
searchInputKey = tkinter.StringVar()
searchInput = tkinter.Entry(root, textvariable=searchInputKey)
searchInput.pack()


# 搜索指令
def searchCommand():
    val = searchInput.get()
    print(val)
    print(val.strip())
    if val.strip() == "":
        print('请输入关键字')
        tkinter.messagebox.showinfo("提示", "请输入关键字")
    else:
        mp3 = search.searchMusic(val)
        for item in mp3:  # 列表插入数据
            searchList.insert(0, item)


# 搜索按钮
searchButton = tkinter.Button(root, text="搜索", command=searchCommand)
searchButton.pack()

# 搜到的列表
searchList = tkinter.Listbox(root)
# for item in mp3:  # 第二个小部件插入数据
#     searchList.insert(0, item)
searchList.pack()

# print(search.searchMusic('我们不一样'))

root.mainloop()  # 进入消息循环
