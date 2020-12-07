# -*- coding:utf-8 -*-


#########################
# open(name, mode, buffer)
# mode: 'r' :读模式
#       ‘w’ :写模式
#       'a' :追加模式
#       'b' :二进制模式
#       '+' :读/写模式
#
# buffer: 0 :无缓冲
#         1 :有缓冲
#         大于1：代表缓冲区的大小
#         -1：使用默认缓冲区的大小
#########################
def python_file():
    f = open('file.txt')
    print(f.read())
    f = open('file.txt', 'w')
    f.write('hello world!')
    f = open('file.txt', 'r')
    print(f.read())


if __name__ == '__main__':
    python_file()
