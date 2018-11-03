# coding:utf-8

'''
ssq_V1.0
author:zzg
date: 2018/9/11
pakage:requests, bs4

V_1.1
date: 2018/10/10
增加: 1. 号码次数; 2.次数和及均值。 

'''

import requests
from bs4 import BeautifulSoup

red_num = {
	'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '10': 0,
	'11':0, '12':0, '13':0, '14':0, '15':0, '16':0, '17':0, '18':0, '19':0, '20': 0,
	'21':0, '22':0, '23':0, '24':0, '25':0, '26':0, '27':0, '28':0, '29':0, '30': 0,
	'31':0, '32':0, '33':0,
}
blue_num = {
	'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '10': 0,
	'11':0, '12':0, '13':0, '14':0, '15':0, '16':0,
}

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

				#统计红球号码出现次数
				red_num[str(int(num_list[i].text))] += 1 
			else:
				num = num + '+  ' + num_list[i].text

				#统计蓝色号码出现次数
				blue_num[str(int(num_list[i].text))] += 1

		msg = term_num + '  ' + num + '\n'
		
		#写入
		#with open('ssq.txt', 'a') as f:
		#	f.write(msg)

# 提取号码出现次数的函数
# 参数： n-->关键字， dic-->号码和次数的字典
def times(n, dic):
	return dic[str(n)]

# 把内容写入文档
# file_name:文档路径和名称
# con: 写入的内容
def writer(file_name, con):
	with open(file_name, 'a') as f:
		f.write(con)

# 号码次数写入函数
# 参数 times-->提取次数的函数， dic-->号码和次数的字典
# 统计次数和值，并计算平均值
def write_times(times, dic, file_name):
	i = 1
	sum = 0
	ave_sum = 0
	while i < len(dic)+1:
		msg_times = '第{0}号球出现的次数：{1}'.format(i, times(i, dic)) + '\n'
		
		#和值
		sum += int(times(i, dic))

		# 该号码出现次数写入文档
		writer('ssq_times.txt', msg_times)

		# 循环计数
		i +=1

	# 计算均值
	ave_sum = sum / len(dic)
	# 写入均值
	writer(file_name, "号码出现平均次数：{0}".format(str(ave_sum)+'\n'))


# 红色号码写入
write_times(times, red_num, 'ssq_times.txt')

# 蓝色号码写入
write_times(times, blue_num, 'ssq_times.txt')