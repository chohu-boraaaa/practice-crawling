import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.v.daum.net/v/20170615203441266')
soup = BeautifulSoup(res.content, 'html.parser')

# 태그 검색
soup.find('title')

# select 함수는 리스트 형태로 전체 반환
title = soup.select('title')[0]
print(title)
print(title.get_text())

# 띄어쓰기 있다면 하위 태그 검색
title = soup.select('html head title')[0]
print(title.get_text())

# 이때 바로 직계의 자식이 아니어도 괜춘
title = soup.select('html title')[0]
print(title.get_text())

# > 를 사용하는 경우 바로 아래 자식만 검색
# 바로 아래 자식이 아니므로 에러 발생
#title = soup.select('html > title')[0]
#print(title.get_text())
# 바로 아래 자식 검색
title = soup.select('head > title')[0]
print(title.get_text())

# .은 태그의 클래스 검색
# class가 article_view인 태그 검색
body = soup.select('.article_view')[0]
print(type(body), len(body))
for p in body.find_all('p'):
    print(p.get_text())

# div 태그 중 class가 article_view인 태그 탐색
body = soup.select('div.article_view')[0]
print(type(body), len(body))
for p in body.find_all('p'):
    print(p.get_text())

# div 태그 중 id가 harmonyContainer 태그 탐색
container = soup.select('#harmonyContainer')
print(container)

# div 태그 중 id가 mArticle인 태그의 하위 태그가 article_title인 태그
title = soup.select('div#mArticle div#harmonyContainer')[0]
print(title.get_text())

# 정규표현식 활용 크롤링
import re

res = requests.get('https://news.daum.net/economic#1')
soup = BeautifulSoup(res.content, 'html.parser')

# a태그이면서 href 속성을 갖는 경우 탐색, 리스트 타입으로 links 변수에 저장
links = soup.select('a[href]')
for link in links:
    print(link)
for link in links:
    print(link['href'])
i = 1
for link in links:
    if re.search('http://\w+', link['href']):
        print(i, '.', link['href'])
    i += 1

# 네이버 부동산 아파트명, 가격 가져오기
res = requests.get('https://new.land.naver.com/complexes?ms=37.517408,127.047313,15&a=APT:JGC:ABYG&e=RETAIL')
soup = BeautifulSoup(res.content, 'html.parser')

# a 태그이면서 href 속성 값이 특정한 값을 갖는 경우 탐색
link_title = soup.find_all('div', class_='complex_title')
link_price = soup.find_all('span', class_='price_default')

for num in range(len(link_price)):
    print(link_title[num].get_text(), link_price[num].get_text())