#!urs/bin/env python
# --*-- coding:utf-8 --*--

# 读取文件内的内容
# 返回按行读取的list

import tkinter
import tkinter.messagebox

base = tkinter.Tk()

# 位置、大小
base.geometry('500x250+300+100')
base.resizable(False, False)

base.title("My Test")


# 信息文本
contentVar = tkinter.StringVar(base, 'sdfgs')
contentEntry = tkinter.Entry(base, textvariable=contentVar)
contentEntry['state'] = 'readonly'
contentEntry.place(x=20, y=20, width=100, height=20)

def buttonClick(btn):
	tkinter.message

lb = tkinter.Label(base, text = "Python Label")

lb.pack()

base.mainloop()


