#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter
import socket

class window():
    def __init__(self, root):
        label1=tkinter.Label(root,text='IP')
        label2=tkinter.Label(root,text='PORT')
        label3=tkinter.Label(root,text='DATA')
        label1.place(x=5,y=5)
        label2.place(x=30,y=5)
        label3.place(x=35,y=5)
        self.entryIP=tkinter.Entry(root)
        self.entryIP.insert(tkinter.END,'127.0.0.1')
        self.entryport=tkinter.Entry(root)
        self.entryport.insert(tkinter.END,'1051')
        self.entrydata=tkinter.Entry(root)
        self.entrydata.insert(tkinter.END,'hello')
        self.Recv=tkinter.Text(root)
        self.entryIP.place(x=40,y=5)
        self.entryport.place(x=40,y=30)
        self.entrydata.place(x=40,y=55)
        self.Recv.place(y=115)
        self.send=tkinter.Button(root,text='send',command=self.send)
        self.send.place(x=40,y=80)
    def send(self):
        try:
            self.entryIP.get()
            port=int(self.entryport.get())
            data=self.entrydata.get()
            client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client.send(data)
            rdata=client.recv(1024)
            self.Recv.insert(tkinter.END,rdata.decode())
            client.close()
        except:
            self.Recv.insert(tkinter.END,'error')

root=tkinter.Tk()
window=window(root)
root.mainloop()