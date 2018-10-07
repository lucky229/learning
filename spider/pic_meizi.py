#! \urs\bin\env python
# -*- coding:utf-8 -*-

"""
爬取妹子网的妹子图
Author: zzg
datetime: 2018/5/22  16:54
note:暂时可以爬取妹子网首页24个主题的系列图片，并存贮在每个系列的文件夹下
     暂没加入系列列翻页功能
     2018/5/26更新，加入自动翻页爬取全站图片
"""

import requests
from bs4 import BeautifulSoup
import re, os

all_url = 'http://www.mzitu.com'

#保存地址
path = 'D:/code/spider/meizitu'

#http请求头
Hostreferer = {
    'Referer': 'http://www.mzitu.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

#破解盗链请求头
picreferer = {
    'Referer': 'http://i.meizitu.net/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

#get请求并用bs4解析网页获取相关信息
req = requests.get(all_url, headers=Hostreferer)
req.encoding = 'utf-8'
all_bf = BeautifulSoup(req.text, 'lxml')

#最大页码数
max_page = all_bf.find_all('a', class_='page-numbers')[-2].text

#每页爬取
for i in range(1, int(max_page)+1):
    #每页的地址
    page_url = all_url + '/page/' + str(i)
    #get请求
    page_req = requests.get(page_url, headers=Hostreferer)
    page_req.encoding = 'utf-8'
    #bs4解析
    page_bf = BeautifulSoup(page_req.text, 'lxml')

    #获取当前页各系列的入口链接
    postlist = page_bf.find_all('ul', id='pins')[0].find_all('a', target='_blank')

    #对每页进行解析
    for i in postlist:
        #获取每页中每个系列的名称和链接
        ser_name = i.text
        ser_link = i.get('href')

        if ser_name:
            #获取每个系列
            ser_pic_req = requests.get(ser_link, headers=Hostreferer)
            ser_pic_req.encoding = 'utf-8'
            ser_bf = BeautifulSoup(ser_pic_req.text, 'lxml')

            #每系列最大页数
            pic_max_page = ser_bf.find_all('div', class_='pagenavi')[0].find_all('span')[-2].text

            for i in range(1, int(pic_max_page)+1):
                ser_d_link = ser_link + '/' + str(i)
                ser_d_req = requests.get(ser_d_link, headers=Hostreferer)
                ser_d_req.encoding = 'utf-8'

                #正则获取图片下载地址
                d_link = re.search(r'<img src="(.*?)" alt=', ser_d_req.text).group(1)
                
                #每张图名称
                d_name = re.search(r'/\d{2}/(.*?)$', d_link).group(1)

                d_req = requests.get(d_link, headers=picreferer)

                #用系列名新建系列文件夹
                new_path = os.path.join(path, ser_name)
                if not os.path.isdir(new_path):
                    os.makedirs(new_path)
                    print("Make new path %s" % ser_name)
                    
                #保存图片
                print("Save %s..." % d_name)
                file_name = new_path + '\\' + d_name
                with open(file_name, 'wb') as f:
                    f.write(d_req.content)
