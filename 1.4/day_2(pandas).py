#!/usr/bin/env python
# coding: utf-8

# In[2]:


#데이터 프레임의 행과 열을 바꿈 : 전치 행렬
import pandas as pd


# In[11]:


exam_data = {'이름' : ['서준', '우현', '인아'], '수학' : [90  , 80  , 70  ], '영어' : [98, 89, 95]}
df = pd.DataFrame(exam_data)
print(df)

df.set_index('이름', inplace = True)
print(df)


# In[12]:


df = df.T
print(df)


# In[15]:


# reindex(새로운 인덱스 배열) : 기존의 자료 변경 안함, 새로운 데이터 프레임 반환
dict_data = {'c0' : [1,2,3], 'c1' : [4,5,6], 'c2' : [7,8,9], 'c3' : [10,11,12]}
df = pd.DataFrame(dict_data, index = ['r1', 'r2', 'r3'])
df


# In[22]:


#index 를 ['r0', 'r1', 'r2', 'r3', 'r4']
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index) # 존재하지 않는 인덱스의 값은 Nan으로 채워줌
print(ndf)

#존재하지 않는 인덱스의 값을 0으로 채워줌
ndf1 = df.reindex(new_index, fill_value = 0)
print(ndf1)
#method : ffill 은 이전자료 복사, bfill 은 이후자료 복사
ndf2 = df.reindex(new_index, method = 'ffill')
print(ndf2)
ndf3 = df.reindex(new_index, method = 'bfill')
print(ndf3)


# In[27]:


#reset_index() : 인덱스 초기화
print(df)
print(df.reset_index()) # 기존의 인덱스가 컬럼으로 변환, 인덱스는 초기화
df.reset_index(drop = True) # 기존의 인덱스를 삭제, 인덱스는 초기화
df


# In[30]:


#인덱스를 기준으로 정렬
df.sort_index(ascending = False) # ascending = True로 설정되어 있다.


# In[36]:


# 컬럼을 기준으로 정렬
df.loc['r1', 'c0'] = 2
df.loc['r2', 'c2'] = 14
df.sort_values(by = ['c0', 'c2'], ascending = False)


# In[37]:


# 인덱스를 설정 df.index = []
# 컬럼 명을 설정 df.columns =[]
# 인덱스의 이름을 변경 df.rename({기존 인덱스 : 새로운 인덱스, ..}, inplace=)
# 컬럼 명을 변경 df.rename({기존 컬럼 : 새로운 컬럼}, inplace =)
# 인덱스를 삭제 df.drop([인덱스명], axis = 0)
# 컬럼 삭제 df.drop([컬럼명], axis = 1)
# 새로운 인덱스 이름 부여 : ndf = df.reindex(new_index, [fill_value= 또는 method=])
# 인덱스 제거 df.reset_index([drop = True]) 인덱스를 컬럼으로 변환하지 않음
# 인덱스 기준으로 정렬 df.sort_index([ascending=])
# 컬럼 기준으로 정렬 df.sort_values(by=[컬럼명])


# In[39]:


# 시리즈 연산 : 시리즈 +,-,*,/ 사칙연산 가능 NaN = Not a Number
# 1. 인덱스로 정렬 -> 2. 매칭되는 값에 대해 연산 (NaN이 있으면 무조건 NaN) -> 
# 3. 결과 return (index로 정렬된 상태)


# In[42]:


student = pd.Series({'국어' : 100, '수학' : 90, '영어' : 90})
print(student)
print(student +200)
print(student / 200)


# In[43]:


# 시리즈 연산
student1 = pd.Series({'국어' : 100, '수학' : 90, '영어' : 90})
student2 = pd.Series({'수학' : 90, '국어' : 100, '영어' : 90, '과학' : 100})
print(student1 + student2)


# In[44]:


# 시리즈 연산
import numpy as np
student1 = pd.Series({'국어' : np.nan, '수학' : 90, '영어' : 90})
student2 = pd.Series({'수학' : 90, '국어' : 100, '영어' : 90, '과학' : 100})
print(student1 + student2)


# In[45]:


# 시리즈 연산 method(메서드) : 시리즈.add(시리즈1, fill_value=0)
print(student1.add(student2))


# In[47]:


print(student1.add(student2, fill_value=0)) # NaN값을 0으로 바꿔서 계산해준다


# In[49]:


print(student1.sub(student2, fill_value=0)) #빼기
print(student1.add(student2, fill_value=0)) #더하기
print(student1.mul(student2, fill_value=0)) #곱하기
print(student1.div(student2, fill_value=0)) #나누기


# In[51]:


# 데이터 프레임 연산( +, *, -, /)
# seaborn 에서 dataset 가져오기
import seaborn as sns


# In[60]:


titanic = sns.load_dataset('titanic')
titanic.columns # age, fare 컬럼의 자료만 검색
df = titanic.loc[:, ['age', 'fare']]


# In[63]:


print(df.head(), '\n\n', (df+10).head())


# In[65]:


print(titanic) # NaN 0으로 처리하기 fill_value = 0 붙이기


# In[72]:


# seaborn 에서 titanic 데이터셋 자료를 가져와서
import seaborn as sns
titanic = sns.load_dataset('titanic')
# 'class', 'sex', 'age', 'alive' 컬럼과
# 0행부터 100행까지만 자료를 가지고 오세요
# df에 저장
df = titanic.loc[0:100, ['class', 'sex', 'age', 'alive']]
print(df)
# 인덱스를 'class'로 지정하고 인덱스로 정렬
df.set_index('class', inplace = True)
print(df)
df.sort_index().head()


# In[70]:


titanic.columns


# In[ ]:


df


# In[73]:





# In[89]:


url = 'sample.html'
tables = pd.read_html(url)
print(len(tables))

for i in range(len(tables)):
    print("tables{}".format(i))
    print(tables[i])
    print()


# In[90]:


df = tables[1]
print(df)
df.set_index('name',inplace = True)
print(df)


# In[94]:


# year 컬럼을 기준으로 정렬

df.sort_values(=by'year')


# In[95]:


# csv 파일로 저장
df.to_csv('sample.csv')

#json 파일로 저장
df.to_json('to_json.json')

#excel 파일로 저장
df.to_excel('to_excel.xlsx')

# 여러개의 데이터 프레임을 하나의 엑셀 파일로 저장
writer = pd.ExcelWriter(".to_excel_writer.xlsx")
df.to_excel(writer,sheet_name='sheet1')
df3to_excel(writer,sheet_name='sheet2')
writer.save()


# In[ ]:




