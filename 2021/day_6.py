#!/usr/bin/env python
# coding: utf-8

# In[8]:


from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.weather.go.kr/w/weather/forecast/mid-term.do?stnId=108'
target = request.urlopen(url)

soup = BeautifulSoup(target)
# for location in soup.select('table.table-col'):
for location in soup.select('td.midterm-province'):
    print(location.text)
    print()
for location in soup.find_all('tbody'):
    if location.find('td', class_='midterm-city'):
        print("도시명 : {}, 최저기온 :{}, 최대기온 :{}".              format(location.find('td', class_='midterm-city').text,
                location.find('span', class_='tmn').text,
                 location.find('span', class_='tmx').text))        
    print()
for location in soup.find_all('tr'): 
    if location.find('td', class_='midterm-city'):
        print("도시명 : {}, 최저기온 :{}, 최대기온 :{}".              format(location.find('td', class_='midterm-city').text,
                location.find('span', class_='tmn').text,
                 location.find('span', class_='tmx').text))        


# In[9]:


import requests
from bs4 import BeautifulSoup


# In[10]:


from urllib import request
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20211229'
target = request.urlopen(url)

soup = BeautifulSoup(target)
soup


# In[11]:


import requests
target1 = requests.get(url)
soup1 = BeautifulSoup(target1.text)
soup1


# In[14]:


movie_title = []
movie_point = []
for movie_rank


# In[16]:


import requests
from bs4 import BeautifulSoup


# In[17]:


# naver 영화 순위 url
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20211229'

# url 에서 데이터 가져옴
target = requests.get(url)
soup = BeautifulSoup(target.text)


# In[28]:


movie_title = []
movie_point = []

for line in soup.find_all('tr'):
    title = line.select_one('div.tit5')
    if title:
        movie_title.append(title.get_text().strip('\n'))
        
    point = line.find('td', class_='point')
    if point:
        movie_point.append(point.get_text())
        
# 순위, 영화제목, 평점 출력
for idx, (title, point) in enumerate(zip(movie_title, movie_point)):
    print("{}. {} = {}".format(idx+1, title, point))


# In[29]:


# papago api 를 활용한 번역 프로그램 작성
text='''Yesterday
All my troubles seemed so far away
Now it looks as though they're here to stay
Oh, I believe in yesterday
Suddenly
I'm not half the man I used to be
There's a shadow hanging over me
Oh, yesterday came suddenly
Why she had to go, I don't know
She wouldn't say
I said something wrong
Now I long for yesterday
Yesterday
Love was such an easy game to play
Now I need a place to hide away
Oh, I believe in yesterday
Why she'''


# In[30]:


import requests


# In[57]:


requests_url = 'https://openapi.naver.com/v1/papago/n2mt'

headers = {"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8", 
           "X-Naver-Client-Id" : "FvAwsHRB6fEOmhQxhymW",
           "X-Naver-Client-Secret" : "kcgRvi5nz3"}

# source=ko&target=en&text=만나서 반갑습니다.
params = {"source" : "en", "target" : "ko" , "text" : text}


# In[63]:


response = requests.post(requests_url, headers = headers, data = params)
print(type(response.text))
print(response.text)

res = response.json() # dict  타입으로 데이터 변경
print(type(res))
print(type(response))


# In[64]:


print(res['message']['result']['translatedText'])


# In[84]:


# 학생, 국어, 수학, 영어 점수를 입력 받아 student_dict{} 에 저장한 후 출력

students = []
score_name = ['kor', 'eng', 'math']
def create_student():
    student = {}
    name = input("학생 이름 입력 >")
    student['name'] = name
    if name == 'q':
        return student
    score = list(map(int,input("국어, 영어, 수학, 점수 입력 >").split()))
    for idx, value in enumerate(score):
        student[score_name[idx]] = value
    return student


# In[91]:


while True:
    student = create_student()
    if student['name'] == 'q':
        break
    students.append(student)
    


# In[92]:


for item in students:
    for key in item:
        print("{} : {} \t".format(key, value[key]), end = '')
        print("\n")


# In[83]:


student_append(student)
student_print(students)
student_sum_avg_print(students)

def student_score_get(student):
    for item in students:
        for key in item:
            print("{}:{}\t".format(key,item[key]), end='')
            
        print("총점:{}\t, avg:{}".format(student_get_sum(item), student_get_avg(item)))
        print("\n")
student_print(students)


# In[ ]:


def student_get_sum(student):
    total = 0
    for value in student.values:
        return student['kor']+
        
        
student_score_get(students)
student_score_sum(students)
        sum
def student_print(students):
    for item in students:
        for key in item:
            print("{}:{}\t".format(key, ))
            


# In[87]:


# class 생성 하기 class 클래스명 : ~~~
class student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    def get_sum(self):
        return self.kor + self.eng + self.math
    def get_avg(self):
        return self.get_sum()/3
    def to_print(self):
        return "{}:{}\t {}\n".format(self.name, self.get_sum(), self.get_avg())


# In[93]:


students = []
while True:
    name = input("학생 이름 입력 >")
    if name =='q':
        break
    score = list(map(int, input("국어, 영어, 수학 점수 입력 >").split()))
    kor = score[0]
    eng = score[1]
    math = score[2]
    Student = Student(name, kor, eng, math)
    
Student.print()
total = 0
for student in Student.students:
    total += student.kor + student.eng + student.math
print("전체 인원수 : {}, 총점 : {}, 평균 : {:.3f}.format(student.count, total, total/Student.count)")


# In[97]:


# class 생성하기 class 클래스 명 : ~~~
class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    def get_sum(self):
        return self.kor + self.eng + self.math
    def get_avg(self):
        return self.get_sum()/3
    def to_print(self):
        return"{}:{}\t {}\n".format(self.name, self.get_sum(), self.get_avg())


# In[108]:


students = []
while True:
    name = input("학생 이름 입력 >")
    if name == 'q':
        break
    score = list(map(int, input("국어, 영어, 수학 점수 입력 >").split()))
    kor = score[0]
    eng = score[1]
    math = score[2]
    student = Student(name, kor, eng, math)
    students.append(student)


# In[109]:


for idx, student in enumerate(students):
    print(students[idx].name)
    print(student.to_print())


# In[112]:


class Test:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print("Test class 생성자 ")
    def class_print(self):
        return self. a + self. b + self. c
    
    def class_return(self, a):
        return a
    def __del__(self):
        print("Test class 소멸자")


# In[115]:


a = Test(10,20,30)
a.class_print()

del a


# In[121]:


class Store:
    def __init__(self, 이름, 전화번호, 주소):
        self.이름 = 이름
        self.전화번호 = 전화번호
    def order(self)  


# In[119]:


print("isinstance(student) :", isinstance(student,Student))


# In[122]:


class Student:
    def study(self):
        print("공부를 합니다")
class Teacher:
    def teacher(self):
        print("가르칩니다")


# In[123]:


classroom = [Student(), Teacher(), Student(), Student(), Teacher()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    else:
        person.teacher()


# In[124]:


class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    def get_sum(self):
        return self.kor + self.eng + self.math
    def get_avg(self):
        return self.get_sum() / 3
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_avg())
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()


# In[125]:


students = [
    Student("윤인성", 87, 98, 88),
    Student("연하진", 92, 98, 96),
    Student("구지연", 76, 96, 94),
    Student("나선주", 98, 92, 96),
    Student("윤아린", 95, 98, 98),
    Student("윤명월", 64, 88, 92)    
]
student_a = Student("윤인성", 87, 98, 88)
student_b = Student("연하진", 92, 98, 96)
print("student_a == student_b =>", student_a == student_b)
print("student_a != student_b =>", student_a != student_b)

for student in students:
    print(str(student))
    if student == student_a or student == student_b:
        print(student.name, student.get_sum())


# In[126]:


# 클래스 변수
class Student:
    count = 0
    students = []
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        
        Student.count += 1
        Student.students.append(self)
        
    @classmethod
    def print(cls):
        print("--------학생 목록--------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("-------------------------")
        
    def get_sum(self):
        return self.kor + self.eng + self.math
    def get_avg(self):
        return self.get_sum()/3
    def __str__(self):
        return "{}\t{}\t{:0.3f}".format(self.name, self.get_sum(), self.get_avg())


# In[103]:


class Circle:
    def __init__(self, radius):
        self.__radius = radius #private 변수
    def get_circum(self):
        return self.__radius*2*3.14
    def get_area(self):
        return self.__radius*self.__radius*3.14
    
    def get_radius(self): #게터
        return self.__radius
    def set_radius(self, calue): #세터
        self.__radius = value


# In[127]:


Student("윤인성", 87, 98, 88)
Student("연하진", 92, 98, 96)
Student("구지연", 76, 96, 94)
Student("나선주", 98, 92, 96)
Student("윤아린", 95, 98, 98)
Student("윤명월", 64, 88, 92)

Student.print()   # 클래스의 매서드 또는 함수
print("전체 인원 수 : ", Student.count) # Student 클래 전체의 global 변수


# In[ ]:





# In[105]:


circle = Circle(10)
print(circle.get_area())

print(circle.get_radius())
circle.set_radius(5)
print(circle.get_radius())
circle.set_radius(15)


# In[ ]:





# In[ ]:





# In[ ]:




