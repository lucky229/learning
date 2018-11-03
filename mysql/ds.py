#!urs/bin/env python
# --*-- coding:utf-8 --*--

'''
ds_ssq_V1.0
author:zzg
date: 2018/10/29
pakage:requests, bs4, pymysql, mysql
目的：下载ssq以往数据，并存储在数据库表ssq中
'''
import requests
from bs4 import BeautifulSoup
import pymysql

# 判断新数据是否已存在
def existence(id_num, cursor):
	# id_num字符串，cursor游标
	# sql语句
	sql = 'select id_num from ssq'

	try:
		# 执行sql语句
		cursor.execute(sql)
		results = cursor.fetchall()
		#print(results)
		#for i in results:
		#	print(i)
	except:
		print('Error')


	if tuple([id_num,]) not in results:
		return True
	else:
		return False

# 数据写入数据库
def writer(param):
	# param 元组
	sql = '''insert into ssq(id_num, red_1, red_2, red_3, red_4, red_5, red_6, blue) 
			 values(%s, %s, %s, %s, %s, %s, %s, %s)'''

	try:
		cursor.execute(sql, param)
		db.commit()
	except:
		print("Error")

# 获取总页数
def get_page(url, Hostheaders):
	#获取网页内容
	all_req = requests.get(url, headers=Hostheaders)
	all_req.encoding = 'utf-8'
	all_bf = BeautifulSoup(all_req.text, 'lxml')
	all_list = all_bf.find_all('p', class_='pg')

	#获取总页码
	list_bf = BeautifulSoup(str(all_list[0]), 'lxml')
	a_list = list_bf.find_all('strong')
	page_num = int(a_list[0].text)

	return page_num

# 获取每页的连接地址
def get_urls(page_num):
	host = 'http://kaijiang.zhcw.com/zhcw/html/ssq/'
	link_all = []
	for i in range(1, page_num+1, 1):
		link = host + 'list_' + str(i) + '.html'
		link_all.append(link)

	return link_all

# 获取号码，并将获取的数据写入数据库
def get_nums(link_all):
	for link in link_all:
		link_req = requests.get(link, headers=Hostheaders)
		link_req.encoding = 'utf-8'
		link_bf = BeautifulSoup(link_req.text, 'lxml')
		link_list = link_bf.find_all('td', align='center')

		for i in range(1,len(link_list),5):
			term_num = link_list[i].text
			num_bf = BeautifulSoup(str(link_list[i+1]), 'lxml')
			num_list = num_bf.find_all('em')
			nums = []
			nums.append(term_num)
			for i in range(7):
				nums.append(num_list[i].text)

			# 将新增加的写入数据库
			if existence(term_num, cursor):
				writer(tuple(nums))
			else:
				break



if __name__ == '__main__':

	url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'
	Hostheaders = {
		'User-Agent': 'Chrome/69.0.3497.81 Safari/537.36',
		'Referer':'kaijiang.zhcw.com'
	}

	pages = get_page(url, Hostheaders)
	links = get_urls(pages)

	# 连接数据库test_ssq
	db = pymysql.connect('localhost', 'root', '1111', 'test')

	# 创建游标
	cursor = db.cursor()

	# 获取数据并写入数据库
	get_nums(links)

	#关闭数据库连接
	db.close()