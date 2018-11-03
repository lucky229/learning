#!urs/bin/env python
# --*-- coding:utf-8 --*--

import pymysql
import tkinter as tk

# 表头
list_table = ['序号', '代码', '名称', '操作', '股价', '数量', '金额', '余额', '备注']


content = ''

# 查询按钮
def chaClick():

	global content
	
	db = pymysql.connect('localhost', 'root', '1111', 'test')
	cursor = db.cursor()
	#sql = "select * from ssq where id_num='2018100'"
	sql = "select * from ssq"
	cursor.execute(sql)
	content = cursor.fetchall()
	db.close()
	
	for i in content:
		t_text.insert(index='insert', chars=i)
	return None



# 主体框架
root = tk.Tk()
root.title('股票记账')
root.geometry('630x400+100+100')

num = 0
# 设置表头和输入框
for i in list_table:
	# 设置表头
	l_head = tk.Label(root, text=i, width=8, height=1, bg='yellow')
	l_head.place(x=5+num*70, y=5)

	# 设置输入框
	enter = tk.Entry(root, text=i, width=8, bg='red')
	enter.place(x=5+num*70, y=35)

	num += 1

# button ,提交按钮
b_submit = tk.Button(root, text="提交", width=87, height=1, bg='blue')
b_submit.place(x=5, y=65)

# button ,查询按钮
b_chaxun = tk.Button(root, text="查询", width=87, height=1, bg='grey',command=chaClick)
b_chaxun.place(x=5, y=95)

# 查询输出
t_text = tk.Text(root, width=87)
t_text.place(x=5, y=130)

#var = (('2018100', '02', '11', '14', '15', '29', '33', '02'),)
#t_text.insert(index='insert', chars=var)


if __name__ == "__main__":
    root.mainloop()
    #chaClick()
    #print(content)
