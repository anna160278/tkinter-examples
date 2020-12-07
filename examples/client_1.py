#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import threading
import tkinter
import socket


class ListenThread(threading.Thread):
    def __init__(self, edit, server):
        threading.Thread.__init__(self)
        self.edit = edit
        self.server = server

        def run(self):
            while 1:
                try:
                    client, addr = self.server.accept()
                    self.edit.insert(tkinter.END,
                                     'connect from:%s:%d\n' % addr)
                    data = client.recv(1024)
                    self.edit.insert(tkinter.END, 'receive data:%s \n' % data)
                    client.send(str('i get:%s' % data).encode())
                    client.close()
                    self.edit.insert(tkinter.END, 'close client\n')
                except:
                    self.edit.insert(tkinter.END, 'close connect\n')
                    break


class control(threading.Thread):
    def __init__(self, edit):
        threading.Thread.__init__(self)
        self.edit = edit
        self.event = threading.Event()
        self.event.clear()

    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server.bind(('127.0.0.1', 9999))
        server.listen(2)
        self.edit.insert(tkinter.END, 'connect...\n')
        self.lt = ListenThread(self.edit, server)
        self.lt.setDaemon(True)
        self.lt.start()
        self.event.wait()
        server.close()

    def stop():
        self.event.set()


class window:
    def __init__(self, root):
        self.root = root
        self.butlisten = tkinter.Button(
            root, text='start', command=self.listen)
        self.butlisten.place(x=20, y=15)
        self.butclose = tkinter.Button(root, text='colse', command=self.close)
        self.butclose.place(x=120, y=15)
        self.edit = tkinter.Text(root)
        self.edit.place(y=50)

    def listen(self):
        self.ctr = control(self.edit)
        self.ctr.setDaemon(True)
        self.ctr.start()

    def close(self):
        self.ctr.stop()


root = tkinter.Tk()
window = window(root)
root.mainloop()
