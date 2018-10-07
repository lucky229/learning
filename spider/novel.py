import requests
from bs4 import BeautifulSoup
import re



    
def writer(contents):
    #写入内容
    file_name = '小说.txt'

    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(contents)
    
    
    
def get_contents(server):
    #server = 'https://www.booktxt.net/4_4496/1631224.html'
    headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
                }

    req = requests.get(server, params=headers)
    req.encoding = 'gbk'
    html = req.text
    div_bf = BeautifulSoup(html, 'lxml')

    #章节名
    name_html = div_bf.find_all('div', class_='bookname')[0]
    name = name_html.find('h1').text
    #print(name)

    #章节内容
    contents = div_bf.find_all('div', id='content')[0].get_text()
    #print(contents)
    return contents
    

if __name__ == '__main__':    
    #获取章节链接
    url = 'https://www.booktxt.net'
    server = 'https://www.booktxt.net/4_4097/'
    req = requests.get(server)
    codedet = req.encoding
    req.encoding = 'ytf-8'
    html = req.text
    div_bf = BeautifulSoup(html, 'lxml')
    names = div_bf.find_all('div', id='list')[0]
    a_bf = BeautifulSoup(str(names), 'lxml')
    a = a_bf.find_all('a')

    
    num = 0
    for i in range(len(a)):
        if "第一章" in a[i].text:
            num = i

    for i in a[num:]:
        writer(i.text + '\n')
        target = url + i.get('href')
        content = get_contents(target)
        writer(content)
        
        
    
