#!/usr/bin/env python
# coding: utf-8

# In[1]:


#표준 모듈 삽입
import math


# In[3]:


print(math.cos(10))
print(math.ceil(5.6)) # 숫자보다 큰 정수 중에 가장 작은 정수(올림)
print(math.floor(5.6)) # 숫자보다 작은 정수 중에 가장 큰 정수(버림)


# In[4]:


# from 모듈명 import 필요한 변수 또는 함수
from math import cos, ceil, floor

print(cos(10))
print(ceil(5.6))
print(floor(5.6))


# In[5]:


# as 를 사용하여 별명(alias) 사용
import math as m
m.cos(10)


# In[13]:


# random 모듈 : 임의의 수를 발생시키는 함수들을 가진 모듈
import random as rnd

print("random 모듈 :")

# random() : 0.0 < x < 1.0 사이의 float 리턴
print("random() : ", rnd.random())

# uniform(min, max) : min < x < max 사이의 float 리턴
print("uniform() : ", rnd.uniform(10,20))

# randrange([min,] max) : min < x < max 사이의 int 리턴, 0부터 max
print("randrange() : ", rnd.randrange(10,20))

# choice(list) : 리시트 내부의 임의의 요소를 리턴
print("choice() : ", rnd.choice(list(range(10))))

# shuffle(list) : 리시트 요소를 랜덤하게 섞음
a = list(range(10))
print("shuffle() : ", rnd.shuffle(a),a)

# sample(list, k=숫자) : 리스트에서 숫자의 갯수 요소를 랜덤하게 리턴
print("sample() :", rnd.sample(a, k = 3))


# In[15]:


# sys 모듈 : 시스템 관련 정보를 가저욤
import sys

print("copyright : ", sys.copyright)
print("version : ", sys.version)


# In[16]:


# os 모듈 : 운영체제와 관련된 명령어
import os

print("현재 운영 체제 :", os.name)
print("현재 작업 경로: ", os.getcwd())
print("현재 폴더 리스트 : ", os.listdir())


# In[20]:


# 디렉토리 생성
os.mkdir('testi_dir')
os.listdir()


# In[21]:


# 디렉토리 삭제
os.rmdir('testi_dir')
os.listdir()


# In[22]:


# file 이름 변경 : rename(old_name, new name)
os.rename('test_dir', 'testi_dir')
os.listdir()


# In[23]:


#file 삭제 : remove(파일명)
#os.remove('new.py')
#os.listdir()
os.system('dir')


# In[24]:


get_ipython().system(' cd dataset')


# In[29]:


# datatime 모듈 : 날짜를 형식에 맞게 편집 가능
import datetime as dt

print(dt.datetime.now())
print(dt.datetime.today())


# In[33]:


# time 모듈 : 일정 시간 멈춤...
import time
print("time start ")
time.sleep(3)
print("/ntime end")


# In[34]:


# urllib 모듈 : url 라이브러리
# 인터넷 검색 1.
from urllib import request

#urlopen() 구글의 메인 페이지 read
target = request.urlopen('http://www.google.com')
output = target.read()

print(output)


# In[108]:


# beautifulsoup4 모듈 설치하는 방법
pip install 모듈(패키지명)
get_ipython().system('pip install beautifulsoup4')


# In[109]:


# <html> ~ </html> tag 형식으로 변환해 주는 모듈 : BeautifulSoup
from bs4 import BeautifulSoup
target = request.urlopen('http://www.google.com')
soup = BeautifulSoup(target)  


# In[110]:



# <title> The Dormouse's story</title>

# soup.title

#soup.

soup.title

soup.title.name

soup.title.string


# In[111]:


# 기상청 날씨 예보를 가져와서 보여줌
# url에 연결 -> urllib.request.urlopen(url명)
#
#
from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.weather.go.kr/w/weather/forecast/short-term.do'
target = request.urlopen(url)

soup = BeautifulSoup(target)


# In[ ]:





# In[112]:


# for location in soup.select('table.table-col'):
for location in soup.select('td.midterm-province'):
    print(location.text)
    print()


# In[105]:


for location in soup.select("table.table-col"):
    print(location)
    for tbody in location.select('tbody'):
        print(tbody)
        
    print("도시 : ", location.select_one('td').text)
    print("구름 : ", location.select_one('td').text)


# In[106]:



for location in soup.findall('tr'): 
    if location.find('td', class='midterm-city'):
        print("도시명 : {}, 최저기온 :{}, 최대기온 :{}".              format(location.find('td', class='midterm-city').text,
                location.find('span', class='tmn').text,
                 location.find('span', class_='tmx').text))


# In[107]:


for location in soup.find_all('tr'):
    if location.find('td', class_='midterm-city'):
        print("도시명 : {} , 최저기온 : {}, 최대기온 : {}".format(location.find('td', class_='midterm-city').text))
        print(location.find('span', class_='tmn').text)
        print(location.find('span', class_='tmx').text)
    print()


# In[93]:


#test 모듈 생성
PI = 3.14

def number_input():
    output = input("숫자 입력 >")
    return float(output)
def get_circum(radius):
    return radius * PI * 2

def get_circle_area(radius):
    return radius * radius * PI

# 활용 예
if __name__ =="__main__":
    print("get_circum(10): ", get_circum(10))
    print("get_circle_area(10):", get_circle_area(10))


# In[94]:


get_ipython().system('pip install flask')


# In[ ]:





# In[95]:


# flask 모듈
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
   return url_report()
def url_report():
   from urllib import

# app.run(host="0.0.0.0", port="5000", debug=True)


# In[96]:


# 모듈 만들기

# 함수 데코레이터
def test(function):
    def wrapper():
        print("Hello start!!!")
        print(function.__name__)
    
        function()
        print(function.__name__)
        print("Hello end !!!")
    print("000:", function.__name__)
    return wrapper
# 데코레이션 함수
@test
def hello():
    print("Hello")

    
# 함수 호출
hello()



# In[97]:


# 내가 만든 패키지 모듈 불러오기
# import 패키지명.모듈명
import test_package.module_a as a
import test_package.module_b as b

print("module_a :", a.variable_a)
print("module_b :", a.variable_b)


# In[98]:


from test_package import *


print("module_a :", module_a.variable_a)
print("module_b :", module_b.variable_b)


# In[99]:


# __all__ =

from test_package import *

print("module_a :", module_a.variable_a)
print("module_b :", module_b.variable_b)


# In[ ]:




