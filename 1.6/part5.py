#!/usr/bin/env python
# coding: utf-8

# In[13]:


# 누락데이터 처리
import pandas as pd
import seaborn as sns


# In[14]:


df = sns.load_dataset('titanic')
df.info()


# In[9]:


# deck 컬럼의 값들의 갯수를 세어봄 df.value_counts(): 유니크한 값들의 갯수
print(df['deck'].value_counts())
print()
deck_cnt = df['deck'].value_counts(dropna = False) # NaN 데이터 세기
print(deck_cnt)
print()

# isnull() 메서드로 누락된 데이터 찾기, null 이면 True, 값이 있으면 False 반환
print(df['deck'].head().isnull())

# isnull()과 sum()함수를 이용하여 누락된 데이터 갯수 찾기
print(df['deck'].isnull().sum)
df.isnull().sum(axis=0) # age, deck, embarked, embark_town -> null data 포함


# In[11]:


# 반복문으로 Nan 데이터 개수 계산하기
nan_data = df.isnull()
for col in nan_data.columns:
    nan_cnt = nan_data[col].value_counts() # 각 열의 Nan갯수 파악
    
    try:
        print(col, ':', nan_cnt[True]) # Nan 값이 존재하면 개수를 출력
    except:
        print(col, ':', 0) #Nan  값이 없으면 0을 출력
        
# Nan 데이터 확인 -> 어떻게 처리할것인지?
# Nan 데이터가 있는 컬럼을 삭제할것인지 / Nan 데이터가 있는 행을 삭제할 것인지


# In[21]:


# df.dropna() : axis = 1 열을 삭제, axis = 0 행을 삭제
# dropna() : Nan이 존재하는 컬럼을 삭제, 갯수가 500 이상인 컬럼만 삭제
df_thresh = df.dropna(axis=1, thresh=500)
df_thresh.info()

# age에 Nan이 존재하는 행을 삭제
df_age = df.dropna(subset=['age', 'embarked'], how='any', axis='index')
df_age.info()

# 컬럼 리스트 : Nan이 존재하는 컬럼리스트
nan_col = [df.isnull().sum()>0]
# Nan 이 존재하는 모든 행을 삭제
nan_col_names = df.columns[nan_col]
#nan_col_name
df_nan= df.dropna(subset=nan_col_names, how = 'any', axis=0)
df_nan.info()
df.isnull()


# In[26]:


sr= pd.Series([1,2,3,4,5])
sr_mask=[True, False, True, True, False]
sr[sr_mask]  # True만 셈, 또한 뒤에 .sum()을 붙이면 항목들을 더함


# In[27]:


df.columns[df.isnull().sum()>0] # Nan이 존재하는 컬럼명만 추출


# In[33]:


# 누락 데이터 치환 : df.fillna(값 또는 mothod =ffill/bfill, inplace = True)
print(df['age'].isnull().sum()) # Nan이 존재함

#Nan이 입력된 age를 평균 나이로 치환
df_age = df.copy()
df_age['age'].fillna(df['age'].mean(axis=0), inplace=True)
df_age['age'].isnull().sum()
print(df['age'].head(), df_age['age'].head(10))


# In[41]:


# 누락 데이터 치환
# embark_town 825~831 행 출력
# 가장 빈번하게 나오는 값으로 치환
df.embark_town[825:832]
df['embark_town'].value_counts().idxmax()# 가장 빈번하게 발생하는 인덱스명
df_em = df.copy()
df_em['embark_town'].fillna(df_em['embark_town'].value_counts().idxmax(), inplace=True)
df_em.embark_town[825:832]


# In[52]:


# 누락 데이터 치환 : 이전 데이터로 치환
df=sns.load
df_me = df.copy()
df_me.embark_town.fillna(method = 'ffill', inplace = True)

print(df_me.embark_town[[828, 829]], '\n',df.embark_town[[828, 829]])


# In[61]:


# 중복 데이터 처리 : df.duplicated() -> 중복 여부 확인
df1 = pd.DataFrame( {'c1' : ['a', 'a', 'b', 'a', 'b'],
                    'c2' : [1,1,1,2,2],
                    'c3' : [1,1,2,2,2]})
print(df1)
df_dup = df1.duplicated()
col_dup = df1['c1'].duplicated()

# 중복된 데이터를 제거, 행을 제거
df2 = df1.drop_duplicates()
print(df2)

# 중복된 컬럼을 제거
df3 = df1.drop_duplicates(subset=['c2', 'c3'])
print(df3)


# In[15]:


# titanic 에서 age, fare, class, alive 컬럼만 가져와서 df_titanic으로 저장한 후
df_titanic = df.loc[:, ['age', 'fare', 'class', 'alive']]
df_titanic.head()


# In[16]:


df_titanic.info()


# In[17]:


# Nan 있는 컬럼의 값의 숫자는 평균으로 문자는 이전 값으로 대체
for col in df_titanic.columns:
    if df_titanic[col].dtype == 'float64':
#        print("float64", col)
        df_titanic[col].fillna(df_titanic[col].mean(), inplace=True)
    else:
#        print("not float64", col)
        df_titanic[col].fillna(method='ffill', inplace = True)
df_titanic.head(6)
len(df_titanic)
# 중복된 행과 컬럼은 삭제하세요
df_titanic.drop_duplicates(inplace=True)
len(df_titanic)


# In[18]:


df_titanic.drop_duplicates(subset=['age'], inplace=True)
len(df_titanic)


# In[23]:


import pandas as pd


# In[26]:


# dataset/ auto_mpg.csv
# 데이터 표준화
df = pd.read_csv('dataset/auto-mpg.csv',header=None)

# 컬럼 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
df.info()
df.head()


# In[29]:


# 단위 환산 : mpg -> gallon => kg으로 변환
mpg_to_kg = 1.60934 / 3.78541
df['kpl'] = df['mpg']*mpg_to_kg
df.head(2)


# In[36]:


# 자료형 변환 : object -> float 으로 변경
df['horsepower'].unique() # 중간에 '?' 발견 - > nan으로 변경, nan 처리함수 사용가능


# In[37]:


import numpy as np
df['horsepower'].replace('?', np.nan, inplace = True)


# In[38]:


# 데이터 타입을 float으로 변경
df['horsepower'] = df['horsepower'].astype('float')


# In[46]:


# origin
df.origin.unique() # 숫자를 category로 변경 : 제조국 이름으로 변경
df.origin.replace({1:'USA', 2:'EU', 3: 'JPN'}, inplace = True)
df.origin.unique()

# object를 카테고리로 변경
df.origin = df.origin.astype('category')
df.info()


# In[47]:


df.info()


# In[48]:


# 제조 년도 : model year -> 카테고리로 변경
df['model year'].unique()


# In[49]:


# 숫자를 문자로, 문자를 category로 변경(순서)
df['model year'] = df['model year'].astype('category')
df.info()
df['model year'].unique


# In[ ]:


# 데이터 전처리
# 1. 누락 데이터 처리 : 제거, 치환
# 2. 중복 데이터 처리 : 제거(행), 컬럼..
# 3. 자료 표준화
#     1) 단위 환산
#     2) 자료형 변경 : object 를 float, object 를 category 로 등등
#        2-1) 변환 불가능한 자료는 NaN으로 치환하고 자료형 변경

