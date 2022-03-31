# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

# 蒐集新聞頁面連結 (模仿封包獲取網頁資訊)
new_list = []

url = 'https://money.udn.com/money/index'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'}
# F12 => 網路 => 右邊頁面 => 擋頭 => 往下拉找到 User-Agent
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
#print(response.text)
div_tag = soup.find_all('div')
soup2 = BeautifulSoup(str(div_tag), 'html.parser')
a_tags = soup2.find_all('a')

for i in a_tags:
    print('title: {}, link: {}'.format(i.text, 'https://money.udn.com'+i['href']))
    new_list.append('https://money.udn.com'+i['href'])


# 爬取新聞內容+圖片
from time import sleep
import os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def save_news(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'}

    response = requests.get(url, headers=headers)
    sleep(1)
    soup = BeautifulSoup(response.text, 'html.parser')
    new_title = soup.find_all('h1', {'id': 'story_art_title'})

    save_path = './news/' + new_title[0].text.replace(':', '')

    article_body = soup.find_all('section', {'id': 'article_body'})
    print('new title: {}'.format(new_title[0].text))

    ## create folder
    createFolder(save_path)
    soup2 = BeautifulSoup(str(article_body[0]), 'html.parser')

    ## save article contens in folder
    with open(save_path + '/contents.txt', 'w', encoding='utf-8') as f:
        p_tags = soup2.find_all('p')
        print('new content: ')
        for i in p_tags:
            print(i.text)
            f.write(i.text)

    ## save image in article
    img_tags = soup2.find_all('img')
    print('save image: ')
    for i in img_tags:
        print(i['src'])
        urlretrieve(i['src'], save_path + '/' + i['title'] + '.jpg')
    print('==========\n\n')

# 測試連結
new_list2 = ['https://money.udn.com/money/story/5612/6186312?from=edn_hottest_index?from=edn_hotlist_index']

for new_url in new_list2:
    print(new_url)
    save_news(new_url)