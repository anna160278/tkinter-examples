# -*- coding: utf-8 -*-
import tkinter as tk

root = tk.Tk()
root.geometry('450x500')
root.configure(bg='grey60')
root.title('my notepad')

# prepare base kwargs
common = dict(
    font='arial 18 bold',
    borderwidth=0,
    wrap='word',  # or 'char', 'none'
    relief='flat',
    tabs='1c',
    highlightthickness=2,
    insertwidth=4,  # fat caret
    insertofftime=600,  # caret slow blink
    insertontime=1200,
    padx=10,  # thick padding
    pady=10,
    blockcursor=False  # make True for really fat cursor
)

# prepare light kwargs
lightmode = dict(
    foreground='black',
    background='white',
    insertbackground='black',  # caret color
    selectforeground='white',  # when text is selected
    selectbackground='black',  # ~
    highlightbackground='gray40',  # highlight color when Text does NOT have focus
    highlightcolor='gray80',  # highlight color when Text has focus
)

# prepare dark kwargs
darkmode = dict(
    foreground='white',
    background='black',
    insertbackground='white',  # caret color
    selectforeground='black',  # when text is selected
    selectbackground='white',  # ~
    highlightbackground='gray80',  # highlight color when Text does NOT have focus
    highlightcolor='gray40',  # highlight color when Text has focus
)

# not used but acts as an example
# that you can just keep copy/pasting these things
# and changing values
mcdonaldsmode = dict(
    foreground='yellow',
    background='red',
    insertbackground='yellow',  # caret color
    selectforeground='red',  # when text is selected
    selectbackground='yellow',  # ~
    highlightbackground='red',  # highlight color when Text does NOT have focus
    highlightcolor='yellow',  # highlight color when Text has focus
)

# toggle modes


def toggle():
    text.basemode = not text.basemode
    text.configure(
        **lightmode) if text.basemode else text.configure(**darkmode)


tk.Button(root, text='Switch Theme', bg='grey60',
          fg='grey100', command=toggle).pack(anchor='e')

text = tk.Text(root, **lightmode, **common)
text.basemode = True  # invent a switch to toggle
text.pack()

root.mainloop()
