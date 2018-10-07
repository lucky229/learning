# coding:utf-8

'''
ssq
author:zzg
date: 2018/9/11
pakage:requests, bs4

'''

import requests
from bs4 import BeautifulSoup

url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'
Hostheaders = {
    'User-Agent': 'Chrome/69.0.3497.81 Safari/537.36',
    'Referer':'kaijiang.zhcw.com'
}


#获取网页内容
all_req = requests.get(url, headers=Hostheaders)
all_req.encoding = 'utf-8'
all_bf = BeautifulSoup(all_req.text, 'lxml')
all_list = all_bf.find_all('p', class_='pg')

#获取总页码
list_bf = BeautifulSoup(str(all_list[0]), 'lxml')
a_list = list_bf.find_all('strong')
page_num = int(a_list[0].text)

#获取每页的网页地址
host = 'http://kaijiang.zhcw.com/zhcw/html/ssq/'
link_all = []
for i in range(1, page_num+1, 1):
	link = host + 'list_' + str(i) + '.html'
	link_all.append(link)


#当前页的内容和号码的代码
for link in link_all:
	link_req = requests.get(link, headers=Hostheaders)
	link_req.encoding = 'utf-8'
	link_bf = BeautifulSoup(link_req.text, 'lxml')
	link_list = link_bf.find_all('td', align='center')

	for i in range(1,len(link_list),5):
		term_num = '第' + link_list[i].text + '期:'
		num_bf = BeautifulSoup(str(link_list[i+1]), 'lxml')
		num_list = num_bf.find_all('em')
		num = ''
		for i in range(7):
			
			#仅有篮球数据
			#if i == 6:
			#	num = num + ' ' + num_list[i].text
			
			# 全部红球和篮球数据
			if i != 6:
				num = num + num_list[i].text + '  '
			else:
				num = num + '+  ' + num_list[i].text

		msg = term_num + '  ' + num + '\n'
		
		#写入
		with open('ssq.txt', 'a') as f:
			f.write(msg)

