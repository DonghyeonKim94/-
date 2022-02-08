#!/usr/bin/env python
# coding: utf-8

# In[4]:


# 팩토리얼 함수 구현
def factorial(n):
    output = 1
    for i in range(1,n+1):
        output*= i
    return output


# In[6]:


# 팩토리얼 함수 구현
def factorial1(n):
    # n이 0이면 1을 return 아니면 n*f(n-1)
    if n ==0:
        return 1
    else:
        return n * factorial1(n-1)


# In[10]:


print(factorial(5)) # factorial 실행
print(factorial1(5))


# In[16]:


# 피보나치 수열 -> f(n) = f(n-1) + f(n-2), n==1, n==2
def fibo(n):
    global count
    count += 1
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


# In[20]:


# 피보나치 수열 -> f(n) = f(n-1) + f(n-2), n==1, n==2
dictionary = {1:1, 2:1}
def fibo_m(n):
    global count
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibo_m(n-1) + fibo_m(n-2)
        dictionary[n] = output
        return output


# In[21]:


fibo(30)


# In[41]:


count = 0
fibo(20)
print("count : ", count)
count = 0
fibo_m(15)
print("count :", count)
print(dictionary)


# In[27]:


[a,b] = [10,20]
(c,d) = (10,20)


# In[36]:


print("a:", a)


# In[38]:


print("d:",d)


# In[43]:


# tuple : 수정할 수 없는 자료(),
tuple_test = (10, 20, 30, 40)
for value in tuple_test:
    print(value)
print(tuple_test[0])
# tuple_test[0] = 10      error
a,b,c = 10,20,30
print("a:{}, b:{}, c:{}".format(a,b,c))

a,b = 10,20
print("before => a:{}, b:{}".format(a,b))
a,b = b,a
print("after => a:{}, b:{}".format(a,b))


# In[47]:


for (idx,value) in enumerate([1,2,3,4,5]): # 튜플을 리턴하는 함수 enumerate
    print("{}번째 값 : {}".format(idx, value))
a, b = divmod(88,3)
print("88 / 3 = {}, {}".format(a,b))


# In[57]:


def call_10_times(func):
    for i in range(10):
        func()
        

    
#map 과 filter 함수 => map(함수,리스트), filter(함수,리스트)
def power(n):
    return n*n
def under_3(n):
            return n<3

#lamda  함수로 변경 -> lambda 매개변수 : 리턴값
power = lambda x: x*x
under_3 = lambda x:x<3
    
a_list = [1,2,3,4,5]
b_list = list(map(power, a_list))
print(b_list)
c_list = list(filter(under_3, a_list))
print("\n", c_list)


# In[58]:


b_list = list(map(lambda x: x*x, a_list))
b_list


# In[63]:


c_list = list(filter(lambda x: x <3, a_list))
c_list


# In[65]:


# file 처리 : open, close, write, read ..
file = open("a.txt", "w")
file.write("Hello Python file write !!")
file.close()


# In[66]:


#file 처리 : open, close, write, read..
file = open("a.txt", "r")
file_data = file.read()
print(file_data)


# In[70]:


# 파일을 자동으로 close() 시킴
with open("a.txt", "w") as file:
    file.write("with python file open!!\n")
    file.write("with python file open!!\n")
    file.write("with python file open!!\n")
# error     file_data = file.read() (with)가 끝났기 때문


# In[71]:


#저장된 파일의 내용을 라인 단위로 읽어옴 
with open("a.txt", "r") as file:
    for line in file:
        print(line)


# In[ ]:


#키보드에서 이름 성적을 입력받아 파일에 저장
with open("score.txt", "w") as file:
    name, score = input("이름 성적 입력 > ").split()
    file.write(name + ',' + score)


# In[ ]:





# In[75]:


with open("score.txt", "r") as file:
    for line in file:
        name, score = line.split(',')
        print(name, ':', score)


# In[86]:


file = open("score.txt", "w+")
name, score = input("이름 성적 입력 > ").split()
file.write(name + ',' + score + '\n') # 파일의 마지막 위치를 가리킬

file.seek(0, 0) #파일의 처음 위치로 이동
for line in file:
    name, score = line.split(',')
    print(name, ': ', score)
file.close()


# In[99]:




def file_write(file):
    while True:
        name = input("이름 입력 >")
        if name == 'q':
            return
        # 30 40 50 - > 문자열 분리 후 "30, 40, 50" 의 형식으로 join
        score = ','.join(input("점수 3과목 입력 >").split())
        file.write(name + ',' + score + '\n')

#검색할 이름의 점수 출력

def file_search(file):
    s_name = input("검색할 이름 입력 > ")
    file.seek(0,0) # 파일의 위치를 처음으로 이동
    for line in file:
        f_data = line.split(',') # f_data = ['name', '90', '80', '100']
        if f_data[0] == s_name:
            return s_name, f_data[1:]
    return None, None

def file_total(file):
    total = 0
    count = 0
    file_seek(0,0)
    for line in file:
        count += 1
        f_data = line.split(',')
        #f_score = list(map(lambda x: int(x), [ x for x in f_data[1:] ]))
        f_score = [int(x) for x in f_data[1:]]
        total+= sum(f_score)
    return total, count


# In[107]:


#file open
file = open("score_tot.txt", "a+")
name, score = input("이름 성적 입력 > ").split()
file_write(name + ',' + score + '\n')
file_seek(0,0)
for line in file:
    name, score = line.split(',')
    print(name, ': ', score)
file.close()


# In[108]:


name, score = file_search(file)
if name:
    print("{}의 성적은 {}, {}, {}".format(name, score[0], score[1], score[2]))
else:
    print('검색된 자료 없음')
    
    
total, count = file_total(file)
print("총 인원수 : {}\t 총 점 : {:5.2f},  평 균 : {:5,2f}").format(count,total/3, total/3/count)


# In[114]:


# 제너레이터 함수 실행 : next(함수명), 함수 내부에 return 대신 yield 사용
def test():
    print("함수 호출 !!")
    yield "test"
    
    print("함수 2222")
    yield "222"
# 함수 호출
print("first call function")
test() # 제너레이터 함수는 일반적인 호출로 실행이 되지 않는다.

print("second call funvion")
test()

file_name = test()
a = next(test())
print(a)    
print("next ---")
b = next(file_name)
print(b)


# In[117]:


numbers = list(range(1, 10+1))

print("#홀수만 출력하기")
print(list(filter(lambda x : x%2, numbers)))
print()

print("#3 이상, 7 미만 추출하기")
print(list(filter(lambda x : 3 <= x < 7, numbers)))
print()

print("#제곱해서 50미만 추출하기")
print(list(filter(lambda x : x*x <= 50, numbers)))


# In[119]:


#try ~ except 예외상황 발생시 처리
try:
    input_number = int(input("정수 입력 >"))
    
    print("원의 반지름 : ", input_number)
    print("원의 둘레 : ",input_number*3.14*2)
    print("원의 넓이 : ",input_number*input_number*3.14)
except:
    print("입력 오류 !!") #대신에 pass라고 써두면 말그대로 pass한다.


# In[120]:


#try except: pass
list_data = ['52', '345', 'test', '123', '44']
# 숫자만 리스트에 추가
list_number = []
for item in list_data:
    try:
        float(item)   # 숫자는 float으로 변환
        list_number.append(item)
    except:
        pass
    
print(list_number)


# In[121]:


# try ~ except ~ else ~ finally
list_data = ['52', '345', 'test', '123', '44']
# 숫자만 리시트에 추가
list_number = []
for item in list_data:
    try:
        float(item)
        
    except:
        print("에러발생 : ", item)
    
    else:
        list_number.append(item)
    
    finally:
        print("무조건 실행 !!")
        
print(list_number)


# In[122]:


# try ~ except ~ else ~finally 
try:
    input_number = int(input("정수 입력 >"))
    print("원의 반지름 : ", input_number)
    print("원의 둘레 : ", input_number*3.14*2)
    print("원의 넓이 : ", input_number*input_number*3.14)
except Exception as e:
    print(e)
    
finally:
    print("프로그램 종료 !!")


# In[126]:


#try ~ except ~ finally
try:
    file = open("info,txt", "w")
    file.read()  #error 발생
    file.close()
except Exception as e:
    print(e)
finally:
    file.close()
    
print("file.closed : ", file.closed)


# In[128]:


def test():
    print("test 함수 시작 !!!")
    try:
        print("test try start")
        return
        print("try 구문 return 다음 문장")
    except:
        print("except 구문 ")
    finally:
        print("finally 구문 ")
    print("test 함수 end !!")
test()


# In[130]:


while True:
    
    print("while 시작 !!!")
    
    try:
        print("while try start")
        break
        print("try 구문 break 다음 문장")
    
    except:
        print("except 구문")
    
    finally:
        print("finally 구문")     # 무조건 실행
    
    print("while end end ~~")     # 실행 안함

    print("while end !!")


# In[134]:


#여러가지 에러 발생 시 에러 종류별로 처리하는 방법
list_number = [52, 273, 45, 66, 88]

try:     # 에러 발생 가능 코드 구현
    input_number = int(input("정수 입력 >"))
    #리스트의 요소 출력
    print("{}번째 요소 : {}".format(input_number, list_number[input_number]))
except ValueError as ex:
    print("정수를 입력하세요 :", ex)
except IndexError as ex:
    print("리스트의 인덱스 범위 오류 :", ex)
except Exception as ex:
    print("알 수 없는 오류 :", ex)
    


# In[136]:


#raise 객체 : 강제로 에러 발생 시킴
number = int(input("정수 입력 >"))

if number > 0:
    # 양수일 때 아직 미구현 상태
    # raise NotImplementedError
    pass
else:
    #미구현 상태
    raise NotImplementedError
    


# In[141]:


# 이름 전화번호를 파일에 저장하는 프로그램 작성
# 파일 이름은 "dataset/dtelno.txt" 기존에 파일이 존재하면 데이터 추가로
# 전화번호 입력은 숫자 3개를 입력받아 123-456-7897 형식으로 저장,
# 이름과 전화번호는 ''로 분리해서 저장
# 저장이 끝나면 파일을 닫고
# 다시 파일을 open -> 'r'
# 파일의 내용을 화면에 출력
# -- 홍길동 123-456-7897
# try ~ except ~ finally 사용해서 작성을 해 보세요

def file_open(file_path, file_name, file_mode):
    try:
        f_name = file_path + file_name
        file = open(f_name, file_mode)
        return file
    except Exception as ex:
        import os
        os.mkdir(file_path)
        file = open(f_name, file_mode)
        return file
 #           print("file open error", ex)
        
def file_write(file):
    try:
        while True:
            name = input("이름 입력")
            if name == 'p':
                break
            tel_no = '-'.join(input("전화 번호 입력").split())
            file.write(name + '' + tel_no + '\n')
            
    except Exception as ex:
        print("file_write error :", ex)
    finally:
        file.close()
def file_read(file):
    try:
        for line in file:
            name, telno = line.split()
            print("{}의 전화번호는 {}".format(name, telno))
    except Exception as ex:
        print("file_read error : ",ex)
    finally:
        file.close()
        


# In[142]:


import os
os.getcwd()      # 현재 작업하고 있는 경로 확인


# In[ ]:


#with open('./dataset/telno.txt', 'w') as file:
# try:
# except:
# => directory 생성

file_path = 'dataset'
file_name = '/telno.txt'
file = file_open(file_path, file_name, 'a+')
file_write(file)
file = file_open(file_path, file_name, 'r')
file_read(file)


# In[ ]:




