#!/usr/bin/env python
# coding: utf-8

# In[6]:


# range([start_no], end_no, [step]) 함수를 사용한 for 반복문 실행
# range(5)

print("range(5)")
for i in range(5):
    print(str(i)+'= 반복횟수')
    
# range(1,5)
print("range(1,5)")
for i in range(1,5):
    print(str(i)+' = 반복횟수')
    
print("range(1,5)")
for i in range(1,10,2):
    print(str(i)+' = 반복횟수')


# In[13]:


# list 와 for 사용하기
list_a = [273, 32, 103, 68, 90]
for element in list_a:
    print(element)
    
#list의 길이를 range 함수에 적용해서
for i in range(len(list_a)):
    print("{}번쨰 반복 : {}".format(i, list_a[i]))
    
#역으로 리스트의 값을 출력
for i in reversed(range(len(list_a))):
    print("{}번째 반복: {}" .format(i,list_a[i]))
    
# list 의 값을 인덱스와 같이 출력
for idx, value in enumerate(list_a):
    print("{}번째 반복: {} .format(idx, value)")


# In[20]:


# while 표현식:
# while True:
#    print(".", end="")
    
# while문을 for문처럼 사용하기
i = 0
while i < len(list_a):
    print(list_a[i])
    i +=1
    
# 상태를 기반으로 반복문 실행
list_b = [1,2,1,2]
value = 1
while value in list_b: # True 인지 False 인지 판단해서 True이면 while 실행
    list_b.remove(value)
while value in list_b:
    list_b.remove(value)
print(list_b)


# In[4]:


# 이름과 점수를 입력받아 딕셔너리에 저장
# 이름에 'q'가 입력되면 입력 종료
# 검색할 이름을 입력받아 해당 이름이 있으면 이름과 점수 출력
# 검색할 이름이 없으면 '자료 없음'으로 출력

dict_score = {}
while True:
    input_list = input("이름 성적 입력 (\'q\'를 입력하면 종료)").split()
    input_name = input_list[0]
    if input_name == 'q': # 입력 종료
        break
        
    #입력 데이터 수가 2가 아니고 두번쨰 입력자료가 숫자가 아니면 다시 입력

    if len(input_list) != 2 or not input_list[1].isdigit():         
        continue 
    
    dict_score[input_list[0]] = dict_score[int(input_list[1])]
#데이터 검색
search_name = input("검색할 이름 : ")
if search_name in dict_score:
    print("{}의 성적 : {}".format(search_name, dict_score[search_name]))

else:
    print("자료 없음")


# In[10]:


# 계산식을 입력받아 계산 결과를 출력하는 프로그램 작성
# 10 + 20 -> 10 + 20 = 30
# +, -, *, /, %, // 모두 가능하도록 하세요
# 처음 문자에 'q' 가 입력되면 프로그램 종료
while True: # break continue 먼저 쓴다 아니면 먼저 break 아니면 continue 비롯 나머지 진행
    cal_list = input("계산식 입력 ex:10 + 20, q가 입력되면 종료").split()
    if cal_list[0] =='q':
        break
    if len(cal_list) != 3 or not cal_list[1] in '+-*/%':
        continue
    if cal_list[1] == '+':
        result = int(cal_list[0]) + int(cal_list[2])
    elif cal_list[1] == '-': 
        result = int(cal_list[0]) - int(cal_list[2])
    elif cal_list[1] == '*': 
        result = int(cal_list[0]) * int(cal_list[2])
    elif cal_list[1] == '/': 
        result = int(cal_list[0]) / int(cal_list[2])
    elif cal_list[1] == '%': 
        result = int(cal_list[0]) % int(cal_list[2])
        
    print("{} {} {} = {}".format(cal_list[0],cal_list[1],cal_list[2],result))


# In[14]:


import time

number = 0
target_time = time.time() + 5
while time.time() < target_time:
    number += 1
print("5초동안 {}번 실행".format(number))


# In[17]:


# reversed() 함수
list_a = [1, 2, 3, 4, 5]
reverse_a = reversed(list_a)
print(reverse_a)
for i in reverse_a:
    print("{}".format(i))
print("rever second:", reverse_a)
for i in reverse_a:
    print("{}".format(i))
    print(reverse_a)
for i in reverse_a:
    print("{}.format(i)")


# In[23]:


print(list_a)
print(list_a[::-1]) # reverse 처럼 쓴다 원 함수에 지장없다
print(list_a)


# In[24]:


# list의 idx와 value를 동시에 반환 : enumerate(list)
# dict의 key와 value를 동시에 반환 : dict.items()


# In[27]:


# 리스트 내포 : [ i for i in 반복 조건식 ]
array = [i for i in range(10) if i % 2 == 0 ]
print(array)

array = [i for i in range(10) if i % 2] #홀수만
array


# In[32]:


# 1에서 100까지의 홀수의 합과 짝수의 합을 구하세요
odd_sum = sum([i for i in range(100) if i %2])

even_sum = sum([i for i in range(100)if not i %2])
print(odd_sum, even_sum)


# In[1]:


#변수를 선언합니다
number = int(input("정수입력>"))

#if 조건문으로 홀수 짝수를 구분합니다.
if number %2 ==0:
    print("""/
    입력한 문자열은 {}입니다.
    {}는 짝수입니다.""".format(number,number))
    
else:
    print("""/
    입력한 문자열은 {}입니다.
    {}는 홀수입니다.""".format(number,number))


# In[3]:


test = (
"이렇게 입력해도 "
"하나의 문자열 ")
print(test)
#[] 튜플, {}딕셔너리, () 튜플 : 데이터 변경 불가능
if number % 2 == 0:
    print(("입력한 문자열은 {}입니다./n"
          "{}는 짝수입니다.").format(number,number))
else:
    print(("입력한 문자열은 {}입니다./n"
          "{}는 홀수입니다.").format(number,number))


# In[4]:


#[] 리스트, {} 딕셔너리, () 튜플 : 데이터 변경 불가능
a = (1,2,3,4)
a_list = [1,2,3,4]
# a[0] = 2 #튜플은 변경 불가
print(a[0])
a_list[0] = 5


# In[11]:


# 문자열 연결 함수 : 문자열.join(리스트)
list_a = ['1', '2', '3', '4', '5'] # 1-2-3-4-5
join_list = "::".join(list_a)

print(join_list)
join_list.split(sep='::')


# In[14]:


print(20/28)


# In[17]:


numbers = [1,2,3,4,5,6]
r_num = reversed(numbers)
print('reversed_numbers :', r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))


# In[1]:


#전화번호부를 작성
# 이름, 전화번호 입력 : 홍길동 123 456 7896
# 저장은 딕셔너리 이름, 전화번호로 저장 -> 전화번호는 123-456-7896의 형식으로
# 이름에 'q'가 입력되면 입력 종료
# 검색할 이름 입력하면 -> 전화번호를 검색해서 출력, 자료 없음
telno_dict = {}
while True:
    input_data = input("이름 전화번호 입력: 홍길동 010 1234 5678 (종료 : q) >")    .split
    name = input_data[0]
    if name == 'q':
        break
    if len(input_data) != 4:
        continue
    telno = []
    for value in input_data[1:]:
        telno.append(value)
    telno_dict[name] = '-'.join(telno)
print(telno_dict)

#전화번호 검색
search_name = input("검색할 이름 : ")
if search_name in telno_dict:
    print(search_name, ":", telno_dict[search_name])
else:
    print("자료 없음")


# In[2]:


search_name = input("검색할 이름 : ")
if search_name in telno_dict:
    print(search_name, ":", telnodict[search_name])
else:
    print("자료 없음")


# In[7]:


def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")
print_3_times()


# In[11]:


def print_n_times(value, n):
    for i in range(n):
        print(value)
        
print_n_times('test',2)


# In[13]:


print_n_times('test', 2) 


# In[6]:


#변수 순서 일반 가변 기본 매개변수
def print_n_times(*value, n=2):
    for i in range(n):
        print(value)
        

print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍")


# In[ ]:


#add함수, sub함수, mul함수, div함수
def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2


# In[ ]:


while True:
    cal_list = input("계산식 입력 ex:10 + 20, q가 입력되면 종료").split()
    if cal_list[0] == 'q':
        break
    if len(cal_list) != 3 or not cal_list[1] in '+-*/%':
        continue
    if cal_list[1] =="+":
        result = add(int(cal_list[0])), int(cal_list[2])
    elif cal_list[1] =='-':
        result = sub(int(cal_list[0])), int(cal_list[2])
    elif cal_list[1] =='*':
        result = sub(int(cal_list[0])), int(cal_list[2])
    elif cal_list[1] =='/':
        result = sub(int(cal_list[0])), int(cal_list[2])
while True:
    cal_list = input("계산식 입력 ex: 10 + 20, q 가 입력되면 종료").split()
    if cal_list[0] == 'q':
        break
    if len(cal_list) != 3 or not cal_list[1] in '+-*/%':
        continue
        
    result = cal_dict[cal_list[1]](int(cal_list[0]),int(cal_list[2]))
        
if result == 'ERR':
        print("처리 불능")

else:
     print ("{} {} {} = {}".format(cal_list[0], cal_list[1], cal_list[2], result))


# In[16]:


while True:
    cal_list = input("계산식 입력 ex:10 + 20, q가 입력되면 종료").split()
    if cal_list[0] =='q':
        break
    if len(cal_list) != 3 or not cal_list[1] in '+-*/%':
        continue
    if cal_list[1] == '+':
        result = int(cal_list[0]) + int(cal_list[2])
    elif cal_list[1] == '-':
        result = int(cal_list[0]) - int(cal_list[2])
    elif cal_list[1] == '*':
        result = int(cal_list[0]) * int(cal_list[2])   
    elif cal_list[1] == '/':
        result = int(cal_list[0]) / int(cal_list[2])
    elif cal_list[1] == '%':
        result = int(cal_list[0]) % int(cal_list[2])         
    
    print("{} {} {} = {}".format(cal_list[0],cal_list[1],cal_list[2],result))


# In[ ]:


a=['1', '2']
a = list(map)


# In[38]:


def input_data():
    stud_dict = {}
    while True:
        name = input("이름 입력 (\'q\'를 입력하면 종료)")
        if name == 'q' : #입력 종료
            break
        score = input("국어 영어 수학 점수 입력:").split()
        if len(score) != 3:
            continue
        score = list(map(int,score)) # 데이터 타입을 int로 변경
        stu_dict[name] = score
    return stu_dict
        
def input_tot_avg(stu_dict):
    for score in stu_dict.values():
        score.append(sum(score))
        score.append(sum(score))/ len(score)
        return stu_dict

def max_min(stu_dict):
    name_list = []
    tot_list = []
    for name, score in stu_dict.items():
        name_list.append(name)
        tot_list.append(score[3])
        
    max_score = max(tot_list)
    min_score = min(tot_list)
    for idx, score in enumaerate(tot_list):
        if max_score == score:
            max_idx = idx
        if min_score == score:
            min_idx = idx
           
    return min_idx, max_idx, name_list
def avg_count(stu_dict):
    for tot_score in stu_dict.values():
        tot_score += score[3]
    return tot_score


# In[39]:


# 국어 영어 수학 점수를 입력받아 dict에 저장하는 함수
# 이름에 'q'가 입력되면 종료
# 1. 각 사람의 합계와 평균을 구해서 dict에 추가하는 함수
# 2. 전체 학생 중 합계가 최고 점수, 최저점수를 가진 학생의 이름과 점수
# 3. 전체 학생의 평균(소수점 미만 2자리까지만), 인원수를 출력stu_dict = input_data()
stu_dict = input_data()
stu_dict = input_tot_avg(stu_dict)
(min_idx, max_idx, name_list) = max_min(stu_dict)
# 이름 최고점, 최저점 출력
print("max_name : {}, max_score : {}, min_name : {}, min_score : {}".      format(name_list[max_idx],stu_dict[name_list[max_idx]][3], name_list[min_idx], stu_dict[name_list[min_idx]][3]))
print("total_score : {}, 인원수 : {}".format(avg_count(stu_dict), len(stu_dict)))

    
#avg_count()
         


# In[76]:


key_list = ["\'name\'", "hp", "mp", "level"]
value_list = ["\'기사\'", 200, 30, 5]
character = {}
for i in range(len(key_list)):
    print("{} : {}".format(key_list[i], value_list[i])) 


# In[77]:


limit = 10000
i = 1
while True:
    print("{}번째 반복입니다.".format(i))
    i = 1+i
    sum_value = i + 
    


# In[ ]:




