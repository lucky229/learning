# coding:utf-8

'''
ssq
author:zzg
date: 2018/9/11
pakage:requests, bs4

'''

import requests
from bs4 import BeautifulSoup

url = 'https://www.miaobige.com/read/7760/'
url_server = 'https://www.miaobige.com'
Hostheaders = {
    'User-Agent': 'Chrome/69.0.3497.81 Safari/537.36',
    'Referer':'https://www.miaobige.com/book/7760/'
}


#获取章节链接
all_req = requests.get(url, headers=Hostheaders)
all_req.encoding = 'gbk'
all_bf = BeautifulSoup(all_req.text, 'lxml')
div_link = all_bf.find_all('div', id='readerlists')
a_bf = BeautifulSoup(str(div_link[0]), 'lxml')
a_link = a_bf.find_all('a')


for i in a_link:
	name = i.text + '\n'
	link = url_server + i.get('href')
	con_req = requests.get(link, headers=Hostheaders)
	con_req.encoding = 'gbk'
	con_bf = BeautifulSoup(con_req.text, 'lxml')
	con = con_bf.find_all('div', id='content')[0].text + '\n\n'
	msg = name + con
		
	with open('yaoxiang.txt', 'a') as f:
		f.write(msg)