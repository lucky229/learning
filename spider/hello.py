import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

    url = 'http://www.biqugexsw.com/21_21436/'
    num = 0

    req = requests.get(url)
    req.encoding = 'gbk'
    bf = BeautifulSoup(req.text, 'lxml')
    div_bf = bf.find_all('div', class_='listmain')[0]
    a_bf = BeautifulSoup(str(div_bf), 'lxml').find_all('a')

    for i in range(int(len(a_bf))):
        name = a_bf[i].text
        
        if '第一百三十三章' in name:
            num = i

    for i in a_bf[num:]:
        name = i.text
        link = 'http://www.biqugexsw.com' + i.get('href')
        page_req = requests.get(link)
        page_req.encoding = 'gbk'
        page_bf = BeautifulSoup(page_req.text, 'lxml')
        con = page_bf.find_all('div', id='content')[0].text.replace('\xa0'*8, '\n')
        with open('nov.txt', 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.write(con)
'''

url = 'http://www.biqugexsw.com/21_21436/22314717.html'
req = requests.get(url)
bf = BeautifulSoup(req.text, 'lxml')
div_bf = bf.find_all('div', class_='content')[0].text.replace('\xa0'*8, '\n')
print(div_bf)
'''
