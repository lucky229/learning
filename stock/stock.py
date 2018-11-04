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
	
	db = pymysql.connect('localhost', 'root', '1111', 'stock')
	cursor = db.cursor()
	#sql = "select * from ssq where 序号=1"
	sql = "select * from stock_list"
	cursor.execute(sql)
	content = cursor.fetchall()
	db.close()
	
	# 插入表头
	t_text.insert(index='insert', chars=list_table)
	t_text.insert(index='insert', chars='\n')

	for i in content:
		for j in i:
			t_text.insert(index='end', chars=j)
			t_text.insert(index='end', chars='  ')
		t_text.insert(index='end', chars='\n')
	return None

# 清除text内的全部内容
def clear():
    t_text.delete('1.0', 'end')
    return None

def submit():
    entries = [e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get(), e8.get(), e9.get()]

    # 将输入内容写入数据库
    db = pymysql.connect('localhost', 'root', '1111', 'stock')
    cursor = db.cursor()

    sql = """insert into stock_list(代码, 名称, 操作, 股价, 数量, 金额, 余额, 备注)
            values(%s, %s, %s, %s, %s, %s, %s, %s)"""
    try:
        cursor.execute(sql, tuple(entries))
        db.commit()
    except:
        print('Error')
    db.close()

# 删除指定或全部数据
def dele():
    db = pymysql.connect('localhost', 'root', '1111', 'stock')
    cursor = db.cursor()

    sql = 'delete from stock_list where 序号=%d' % int(e10.get())

    if e10.get() == '0':
        cursor.execute('truncate table stock_list')
    else:
        cursor.execute(sql, tuple(entries))

    db.commit()
    db.close()

def submit():
    entries = [e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get(), e8.get(), e9.get()]

    # 将输入内容写入数据库
    db = pymysql.connect('localhost', 'root', '1111', 'stock')
    cursor = db.cursor()

    sql = """insert into stock_list(代码, 名称, 操作, 股价, 数量, 金额, 余额, 备注)
            values(%s, %s, %s, %s, %s, %s, %s, %s)"""
    try:
        cursor.execute(sql, tuple(entries))
        db.commit()
    except:
        print('Error')
    db.close()


# 主体框架
root = tk.Tk()
root.title('股票记账')
root.geometry('630x400+100+100')

num = 0
entries = []
# 设置表头和输入框
for i in list_table:
	# 设置表头
	l_head = tk.Label(root, text=i, width=8, height=1, bg='yellow')
	l_head.place(x=5+num*70, y=5)

	num += 1

# 设置输入框
e1 = tk.Entry(root, width=8, bg='red', textvariable='序号')
e2 = tk.Entry(root, width=8, bg='red', textvariable='代码')
e3 = tk.Entry(root, width=8, bg='red', textvariable='名称')
e4 = tk.Entry(root, width=8, bg='red', textvariable='操作')
e5 = tk.Entry(root, width=8, bg='red', textvariable='股价')
e6 = tk.Entry(root, width=8, bg='red', textvariable='数量')
e7 = tk.Entry(root, width=8, bg='red', textvariable='金额')
e8 = tk.Entry(root, width=8, bg='red', textvariable='余额')
e9 = tk.Entry(root, width=8, bg='red', textvariable='备注')
e1.place(x=5+0*70, y=35)
e2.place(x=5+1*70, y=35)
e3.place(x=5+2*70, y=35)
e4.place(x=5+3*70, y=35)
e5.place(x=5+4*70, y=35)
e6.place(x=5+5*70, y=35)
e7.place(x=5+6*70, y=35)
e8.place(x=5+7*70, y=35)
e9.place(x=5+8*70, y=35)

# 删除后台数据库信息输入框
e10 = tk.Entry(root, width=8, bg='red')
e10.place(x=560, y=130)

# button ,提交按钮
b_submit = tk.Button(root, text="提交", width=87, height=1, bg='blue', command=submit)
b_submit.place(x=5, y=65)

# button ,查询按钮
b_chaxun = tk.Button(root, text="查询", width=87, height=1, bg='grey',command=chaClick)
b_chaxun.place(x=5, y=95)

# button, 清除text里面的内容
b_clear = tk.Button(root, text="清除下述显示内容", width=20, height=1, bg='green',command=clear)
b_clear.place(x=5, y=125)

# button, 删除后台数据库内容
b_del = tk.Button(root, text="删除指定行内容(0为全部）", width=20, height=1, bg='red',command=dele)
b_del.place(x=400, y=125)

# 查询输出
t_text = tk.Text(root, width=87)
t_text.place(x=5, y=170)

#var = (('2018100', '02', '11', '14', '15', '29', '33', '02'),)
#t_text.insert(index='insert', chars=var)


if __name__ == "__main__":
    root.mainloop()
    #chaClick()
    #print(content)
