'''
https://ko.wikipedia.org/wiki/
https://ko.wikipedia.org/wiki/기계_학습 = 문서가 있음
https://ko.wikipedia.org/wiki/NLP = 문서가 여러개
https://ko.wikipedia.org/wiki/Asdf_wfa = 문서 없음
'''

import requests
from bs4 import BeautifulSoup
import re


PAGE_STATS = {
    '1': '문서가 존재하지 않습니다.',
    '2': '이 문서는 명칭은 같지만 대상이 다를 때에 쓰이는 동음이의어 문서입니다', 
    '3': '이 문서의 내용은 출처가 분명하지 않습니다'
    }
    
URL = 'https://ko.wikipedia.org'

def toURL(text):
    # reg = re.compile('[ㄱ-ㅣ가-힣]+')
    # if len(reg.findall(text)):
    #     URL = 'https://ko.wikipedia.org'
    # else:
    #     URL = 'https://en.wikipedia.org'
    return URL + '/wiki/' + text.replace(' ', '%20')

def crawler(text):
    res = []
    req = requests.get(toURL(text))
    soups = [BeautifulSoup(req.text, 'html.parser')]

    td = soups[0].find('td', class_='mbox-text')

    if td:
        if PAGE_STATS['1'] in td.text:
            return None
        if PAGE_STATS['2'] in td.text:
            element = soups[0].find('div', class_='mw-parser-output')
            element = element.find('ul')
            for a in element.find_all('a'):
                req = requests.get(URL + a['href'])
                soups.append(BeautifulSoup(req.text, 'html.parser'))
            del soups[0]
    for soup in soups:
        ul = soup.find('div', id='mw-normal-catlinks').find('ul')
        for a in ul.find_all('a'):
            res.append(a.text)
    return res
