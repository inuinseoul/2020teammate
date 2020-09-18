import requests
import numpy as np
import re
from bs4 import BeautifulSoup


MAX = 3  # 크롤링 할 사전 개수 (높을수록 관련성이 떨어질 수 있음) 

def toURL(text):
    return text.replace(' ', '+')

def crawler(text):

    req = requests.get('https://terms.naver.com/search.nhn', params = (
            ('query', toURL(text)),
            ('searchType', 'text'),
            ('dicType', ''),
            ('subject', ''),
        ))
    soup = BeautifulSoup(req.text, 'html.parser')
    tags = []
    links = []

    for ul in soup.find_all('ul', class_='content_list'):
        element = ul.find('strong', class_='title')
        element = element.find('a')

        if element['href'].startswith('/entry.nhn'):
            links.append('https://terms.naver.com' + element['href'])
            
    for i in range(len(links)):
        if i >= MAX:
            break
        try:
            req = requests.get(links[i])
            soup = BeautifulSoup(req.text, 'html.parser')

            for li in soup.find('ul', id='countControlByHeight').find_all('li'):
                element = li.find('div', class_='desc')
                for a in element.find_all('a'):
                    if a.get('onclick'):
                        tag = re.sub('[^ㄱ-ㅣ가-힣a-zA-Z0-9-]', '', a.text)
                        tag = tag.replace('-', ' ').strip()
                        tags.append(tag)
        except Exception as e:
            print(end='')
            # print(f'{i}번 오류: {e}')
    
    # res = list(set(tags))
    # m = np.array([len(tag) for tag in tags]).mean() * 1.5
    # print(m, np.array([len(tag) for tag in tags]).max())
    # return [x for x in res if float(len(x)) <= m]
    return list(set(tags))