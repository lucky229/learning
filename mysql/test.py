#!urs/bin/env python
# --*-- coding:utf-8 --*--

import pymysql

# 数据库测试

# 查询
def get_num(id_num):
	sql = """select * from ssq where id_num=%s""" % (id_num)

	try:
		cursor.execute(sql)
		results = cursor.fetchall()
	except:
		print('Error')

	print(results)
	print(type(results))

# 判断数据是否已存在
def existence(id_num):
	# sql语句
	sql = 'select %s from ssq' % (id_num)

	try:
		# 执行sql语句
		cursor.execute(sql)
		results = cursor.fetchall()
		#print(results)
		#for i in results:
		#	print(i)
	except:
		print('Error')

	#id_num = '2003012'

	if tuple([id_num,]) not in results:
		print(True)
	else:
		print(False)

if __name__ == '__main__':

	# 连接数据库test_ssq
	db = pymysql.connect('localhost', 'root', '1111', 'test')

	# 使用cursor()方法创建游标
	cursor = db.cursor()

	id_num = '2018102'
	#get_num(id_num)
	get_num(id_num)


	#关闭数据库连接
	db.close()