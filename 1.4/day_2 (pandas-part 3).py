#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 데이터 프레임 살펴보기
import pandas as pd


# In[2]:


df = pd.read_csv('dataset/auto-mpg.csv', header = None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 
              'weight', 'acceleration', 'model year', 'origin', 'name']
df.head()
df.tail()


# In[3]:


# 데이터 프레임의 기본 정보 : info()
df.info()  #인덱스(행)의 갯수, 컬럼(열)의 정보를 보여줌


# In[4]:


# 데이터 프레임의 기술 통계정보 요약 : describe()
df.describe()


# In[5]:


# 각 열의 데이터 갯수 : count(), 실제 값이 존재하는 자료만 count(NaN이 존재하면 count하지 않음)
df.count()


# In[6]:


import seaborn as sns
df = sns.load_dataset('titanic')
df.count(0)


# In[10]:


# 각 열의 고유 값의 갯수 : df[열이름]value_counts()
df['origin'].value_counts()


# In[21]:


# 각 열의 고유 값의 갯수 : df[열이름].value_counts()
df['origin'].value_counts()

# 열의 평균값 : df[열이름].mean()
df['mpg'].mean()

#  각 열의 평균값 : df.mean()
df[['mpg', 'weight']].mean()

# 열의 중간 값 : median()
df.median(numeric_only = True)


# In[20]:


df.corr()


# In[18]:


# 최대 : max(), 최소 : min(), 표준편차 : std(), 분산 : var(), corr()
df.corr()       # df[[컬럼명, ...]].corr()
df.var(numeric_only = True)


# In[27]:


# titanic 자료를 가지고 와서 titanic의 기본정보
titanic_df = sns.load_dataset('titanic')
titanic_df.info()
# 기술통계 요약, 같은 나이의 인원 수
titanic_df.describe()
titanic_df['age'].value_counts().head()
# 전체 데이터의 평균, 중간값, 최대, 최소, 표준편차
print(titanic_df.mean(numeric_only= True))
print(titanic_df.median(numeric_only= True))
print(titanic_df.max(numeric_only= True))
print(titanic_df.min(numeric_only= True))
print(titanic_df.std(numeric_only= True))
# 각 열의 유효한 자료의 갯수 확인하기
print()
print(titanic_df.count())


# In[28]:


# 타이타닉 자료에서 class 가 'first'인 자료만 검색
titanic_df[titanic_df['class'] == 'First' ].loc[ :  , ['class', 'age']]


# In[29]:


titanic_df['class'] == 'First' 


# In[30]:


titanic_df[titanic_df['class'] == 'First']


# In[31]:


# 클래스가 'First'이고 나이가 평균 나이보다 적은 사람의 자료만 출력
# sex, age, class, alive 컬럼만 출력
# a ==10 & b == 20 : pandas 에서는 &(and) 와 | (or) 를 사용


# In[33]:


(titanic_df['class'] == 'First') & (titanic_df['age'].mean() < titanic_df['age'])


# In[34]:


titanic_bool = (titanic_df['class'] == 'First') &                (tutabuc_df['age'].mean() < titanic_df['age'])
df = titanic_df[titanic_bool]

# sex, age, class, alive 컬럼만 출력
df1 = df.loc[:, ['sex', 'age', 'class', 'alive']]
df2 = titanic_df[(titanic_df['class'] == 'First') &                 (titanic_df['age'].mean() > titanic_df['age'])].loc[:,
                                                                    ['sex', 'age', 'class', 'alive']]
df2.info()
df2.describe()
df2.head()
df2['alive'].value_counts()
#


# In[35]:


# 데이터 전처리 작업
# 외부에서 데이터를 가져옴
    # 1. info() : 컬럼의 정보, 데이터의 갯수
    # 2. 통계정보 describe()
    # 3. head() 전체 자료의 5개의 인덱스만 확인
    # 4. NaN 데이터가 있는지 확인 : df.count()
    # 5. NaN 데이터를 처리 (없애거나 뒤의 데이터 앞의 데이터를 가져오거나 등등)
    # 6. df.corr() 데이터간의 상관 관계 확인
    # 7. 그래프로 자료를 확인


# In[42]:


# pandas 에서 제공하는 그래프 함수 plot()
df = pd.read_excel('dataset/남북한발전전력량.xlsx')
df.head(7)


# In[41]:


# 남한과 북한의 1991년 이후 자료만 가져오기
df_ns = df.iloc[[0,5], 3:]
df_ns


# In[39]:


df_ns # 0와 5 인덱스명을 0: 'South' , 5 : 'North' 인덱스 명 변경
df_ns.index = ['South', 'North']
df_ns


# In[44]:


# 데이터의 정보 확인
df_ns.info()  # object를 int 형으로 변경


# In[48]:


df_ns.columns = df_ns.columns.map(int)


# In[50]:


df_ns.columns


# In[54]:


df_ns.plot() # index -> X 축, 년도를 기준으로 남한과 북한의 전력량을 확인
tdf_ns = df_ns.T  # 인덱스와 컬럼의 위치 변환
tdf_ns.head()
tdf_ns.plot()  # 남한과 북한의 연도별 전력량을 그래프로 표시


# In[55]:


tdf_ns.plot(kind='bar')
tdf_ns.plot(kind='hist')


# In[57]:


# auto - mpg.csv 파일을 읽어서 데이터 프레임을 생성, csv 데이터 확인, header
# 컬럼명을 지정을 합니다
# df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 
                #'model year', 'origin', 'name']
# 산점도 kind = 'scatter', x = weight과 y = mpg 컬럼에 대해서
# weight 과 mpg 컬럼의 상관관계도 표시


# In[60]:


df_mpg = pd.read_csv('dataset/auto-mpg.csv', header = None)
df_mpg
df_mpg.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
                 'acceleration', 'model year', 'origin', 'name']
df_mpg
df_mpg[['weight', 'mpg']].corr()

df_mpg.plot(x='weight', y='mpg', kind = 'scatter')
df_mpg.plot(x='mpg', y='displacement', kind = 'scatter')


# In[59]:


df_mpg.corr()


# In[ ]:




