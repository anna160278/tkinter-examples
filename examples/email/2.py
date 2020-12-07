# -*- coding:utf-8 -*-
from tkinter import *
from tkinter.messagebox import askyesno, showerror, showinfo
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import re

def login():

    emailRegex = r"[-_\w\.]{0,64}@([-\w]{1,63}\.)*[-\w]{1,63}"
    try:
        smtp_server = 'smtp.' + \
            re.search(emailRegex, username.get()).group().rsplit('@', 1)[1]
        global server
        server = smtplib.SMTP(smtp_server, 25, timeout=5)
    except Exception as e:
        showerror(title="用户名错误", message="请检查用户名是否正确！")

    # server.set_debuglevel(1)
    try:
        server.login(username.get(), password.get())
        global from_addr
        from_addr = username.get()
        showinfo(title="登录成功", message="恭喜登录成功！")
        global auth
        auth = True
        Label(root, text=from_addr).grid(row=0, column=2, sticky='w')
        tk.destroy()
    except Exception as e:
        showerror(title="登录失败", message="登录失败,请检查用户名或密码是否正确!")
        print(e, '登录失败')
        return False


def logout():
    try:
        global quit
        server.quit()
        quit = 1
    except Exception as e:
        pass


# 邮件发送成功之后的处理
def after_send():
    content.delete(0.0, END)
    sub.delete(0, END)


# 发送邮件
def send():
    try:
        if quit or not auth:
            showinfo(title="未登录", message="请先登录！")
            return 0
        elif auth:
            FROM = 'From:' + from_addr
            TO = 'To:' + to_addr.get()
            SUBJECT = subject.get()
            CONTENT = content.get(0.0, END)

            def _format_addr(s):
                name, addr = parseaddr(s)
                return formataddr((Header(name, 'utf-8').encode(), addr))

            msg = MIMEText(CONTENT, 'plain', 'utf-8')

            msg['From'] = _format_addr(FROM)
            msg['To'] = _format_addr(TO)
            msg['Subject'] = Header(SUBJECT, 'utf-8').encode()
            # server.set_debuglevel(1)
            try:
                server.sendmail(FROM, TO, msg.as_string())
                showinfo(title="发送成功！", message="邮件发送成功！")
                after_send()
                return 0
            except Exception as e:
                showerror(title="发送失败", message=e)
                return e
    except Exception as e:
        showerror(title="错误", message=e)


def login_window():
    global tk
    tk = Toplevel()
    tk.title("邮箱登录")
    tk.resizable(width=False, height=False)
    # 设置logo
    tk.iconbitmap('logo.ico')
    width = 400
    height = 200
    screenwidth = tk.winfo_screenwidth()
    screenheight = tk.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                                (screenheight - height) / 2)
    tk.geometry(alignstr)

    # 定义登录窗口
    Label(tk, text="邮 箱 登 录", font=("Arial", 13),
          fg='green').grid(columnspan=4, pady=20, ipadx=150)
    Label(tk, text="账  号").grid(column=1, sticky='e', pady=5)
    Label(tk, text="密  码").grid(column=1, sticky='e', pady=5)
    Entry(tk, textvariable=username).grid(row=1, column=2, pady=5)
    Entry(tk, textvariable=password, show='*').grid(row=2, column=2, pady=5)

    Button(tk, text="退出", command=tk.quit, fg='red').grid(pady=5,
                                                          row=3,
                                                          column=2,
                                                          sticky='w',
                                                          padx=30)
    Button(tk, text="登录", command=login, fg='green').grid(pady=5,
                                                          row=3,
                                                          column=2,
                                                          sticky='e',
                                                          padx=30)


# 设置收件人和主题
def send_window():
    Button(root, text="发  送", command=send).grid(rowspan=3, padx=10)

    Label(root, text="发件人").grid(row=0, column=1)
    Label(root, text=from_addr).grid(row=0, column=2, sticky='w')

    Label(root, text="收件人").grid(row=1, column=1)
    Entry(root, textvariable=to_addr, width=90).grid(row=1, column=2, pady=5)

    Label(root, text="主  题").grid(row=2, column=1)
    global sub
    sub = Entry(root, textvariable=subject, width=90)
    sub.grid(row=2, column=2, pady=5)

    # 邮件内容
    global content
    content = Text(root, height=35, width=110)
    content.grid(pady=30, padx=10, columnspan=4)

    menu()


def menu():
    top_menu = Menu(root)
    root.config(menu=top_menu)

    account = Menu(top_menu, tearoff=0)
    top_menu.add_cascade(
        label="账号",
        menu=account,
    )
    account.add_command(label="登录", command=login_window)
    account.add_command(label="退出", command=logout)

    choice = Menu(top_menu, tearoff=0)
    top_menu.add_cascade(label="选项", menu=choice)
    choice.add_command(label="插入附件")


if __name__ == "__main__":
    # 创建登录窗口
    root = Tk()
    root.title("邮件发送")
    root.resizable(width=False, height=False)
    width = 800
    height = 600
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                                (screenheight - height) / 2)
    root.geometry(alignstr)
    # 设置logo
    root.iconbitmap('logo.ico')
    auth = False
    server = ""
    quit = 0
    from_addr = "未登录"
    username = StringVar()
    password = StringVar()
    to_addr = StringVar()
    subject = StringVar()

    if not auth:
        if askyesno(title="未登录", message="是否登录？"):
            login_window()
    send_window()
    root.mainloop()