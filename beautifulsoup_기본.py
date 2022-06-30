# BeautifulSoup 라이브러리 : HTML 태그를 파싱해서 필요한 데이터만 추출하는 함수

import re
import requests
from bs4 import BeautifulSoup
import html5lib

# 1. request 라이브러리 활용 HTML 페이지 요청
## res 객체에 HTML 데이터 저장, res.content로 데이터 추출 가능
res = requests.get('https://news.v.daum.net/v/20220630112834744')

# 2. HTML 페이지 파싱 BeautifulSoul(HTML데이터, 파싱방법)
soup = BeautifulSoup(res.content, 'html.parser')
## 필요한 데이터 검색
title = soup.find('title')
print('1. 기사에서 제목 가져오는 예제 : ' + title.get_text())

# 3. htmil 간단한 구조 살펴보고 태그로 콘텐츠 검색
html = '''
<html>
    <body>
        <h1 id='title'>자기소개</h1>;
        <p class='cssstyle'>간단한 자기소개</p>
        <p id='body' align='center'>안녕하세요 쵸후입니다.</p>
    </body>
</html
'''
soup1 = BeautifulSoup(html, "html.parser")
title_data = soup1.find('h1')
print('2. 웹페이지를 태그로 검색하는 방법')
print(title_data)
print(title_data.string)
print(title_data.get_text())

print('\n2-1. 가장 먼저 검색되는 태그 반환')
paragraph_data = soup1.find('p') # p로 시작하는 가장 먼저 검색되는 태그 반환
print(paragraph_data)
print(paragraph_data.string)
print(paragraph_data.get_text())

# 3. HTML 태그와 CSS class 활용해서 필요한 데이터 추출하는 방법1
paragraph_data1 = soup1.find('p', class_='cssstyle')
print('\n3. HTML 태그와 CSS class 활용해서 필요한 데이터 추출하는 방법1')
print(paragraph_data1)
print(paragraph_data1.string)
print(paragraph_data1.get_text())

# 4. HTML 태그와 태그에 있는 속성 이용하여 크롤링
paragraph_data2 = soup1.find('p', attrs = {'align': 'center'})
print('\n4. HTML 태그와 태그에 있는 속성 이용하여 크롤링')
print(paragraph_data2)
print(paragraph_data2.string)
print(paragraph_data2.get_text())

# 5. find_all() : 관련된 모든 데이터를 리스트 형태로 추출하는 함수
paragraph_data3 = soup1.find_all('p')
print('\n5. find_all() : 관련된 모든 데이터를 리스트 형태로 추출')
print(paragraph_data3)
print(paragraph_data3[0].string)
print(paragraph_data3[1].get_text())

# 6. BeautifulSoup 라이브러리 활용 string 검색
## 태그가 아닌 문자열 자체로 검색
## 문자열, 정규표현식 등등으로 검색 가능
### 문자열 검색의 경우 한 태그내의 문자열과 정확하게 매칭되는 것만 추출
#### ex. AI가 포함된 긴 문장의 경우 string='AI'로 검색하면 검색되지 않음
#### 이때는, 정규표현식 이용해야 함.
### 만약 정확하게 매칭이 되지 않는다면 정규표현식 사용
new_res = requests.get('https://news.v.daum.net/v/20220630112834744')
new_soup = BeautifulSoup(new_res.content, 'html5lib') # html5lib 라이브러리 사용
print('\n6. BeautifulSoup 라이브러리 활용 string 검색')
print(new_soup.find_all(string='김동현'))
print(new_soup.find_all(string=['아워홈의 휴화산 \'남매의 난\'..구지은 부회장 행보는?', '김동현']))
print(new_soup.find_all(string='LG'))
print(new_soup.find_all(string=re.compile('LG'))[0])
print(new_soup.find_all(string=re.compile('LG')))

# 7. 연습문제 - 다음 사이트에서 링크가 되어 있는 모든 제목을 가져와서 출력하기
print('\n7. 연습문제')
news_res = requests.get('https://news.daum.net/digital#1')
news_soup = BeautifulSoup(news_res.content, 'html.parser')
news_main = news_soup.find_all('section', class_='inner-main')
for i in news_main:
    news_title = i.find_all('a', class_='link_txt')
for i in news_title:
    print(i.get_text())