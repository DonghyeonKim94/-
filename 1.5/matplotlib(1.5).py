#!/usr/bin/env python
# coding: utf-8

# In[36]:


# 그래프 matplotlib 를 사용
import matplotlib.pyplot as plt
import numpy as np


# In[37]:


# %load font.py
#!/usr/bin/env python

# In[ ]:


import platform
if platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic') 
elif platform.system() == 'Windows': #윈도우
        plt.rc('font', family='Malgun Gothic') 
elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
        plt.rc('font', family='Malgun Gothic') 

plt.rcParams['axes.unicode_minus'] = False #한글 폰트 사용시 마이너스 폰트 깨짐 해결


# In[26]:


import platform
if platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic') 
elif platform.system() == 'Windows': #윈도우
        plt.rc('font', family='Malgun Gothic') 
elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
        plt.rc('font', family='Malgun Gothic') 

plt.rcParams['axes.unicode_minus'] = False #한글 폰트 사용시 마이너스 폰트 깨짐 해결


# In[4]:


f1 = plt.figure(figsize = (10,2)) # 사이즈 : Inch

plt.title('New figure')

plt.plot(np.random.randn(100))
plt.show()


# In[6]:


# subplot : 하나의 페이지에 여러개의 그래프 그림
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
y1 = np.cos(2*np.pi*x1)*np.exp(-x1)
y2 = np.cos(2*np.pi*x2)
ax1 = plt.subplot(2,1,1)
plt.plot(x1, y1, 'yo-')
plt.title(' A table of 2 subplot')
plt.ylabel('damped oscillation')
print(ax1)

ax2 = plt.subplot(2,1,2)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time ')
plt.ylabel('Undamped ')
print(ax2)
plt.show()


# In[8]:


# 선 그래프
# 시도별 진출입 인구수
import pandas as pd

df = pd.read_excel('dataset/시도별 전출입 인구수.xlsx', header = 0)
df.head(20)


# In[15]:


# 전출지의 Nan 자료를 수정 -> 이전 자료의 값으로 대체
# Nan 자료를 수정 : ffill 이전 자료로 대체 bfill : 이후 자료로 대체
# value = 값 -> 지정하는 값으로 수정
df.fillna(method='ffill', inplace=True) 
df.tail(25)


# In[16]:


#2. 필요한 자료만 추출
# 서울 특별시에서 다른 지역으로 전출한 자료만 추출
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
#df_seoul = df[ (df['전출지별'] =='서울특별시') \ & (df['전입지별'] != '서울특별시')]
print(df_seoul.head())
#'전출지별'은 같은 자료이므로 삭제(필요없는 컬럼 삭제)
df_seoul.drop('전출지별', axis = 1, inplace = True)
df_seoul
#3. 


# In[18]:


# '전입지별'을 '전입지'로 변경
df_seoul.rename({'전입지별' : '전입지'}, axis = 1, inplace = True)
# 전입지컬럼을 인덱스로 변경
df_seoul.set_index('전입지', inplace = True)
df_seoul


# In[ ]:


pd.plotting(df_seoul)


# In[39]:


df_seoul.T.plot()


# In[23]:


# 서울에서 경기도로 전입한 인구수를 그래프로 확인
sr_one = df_seoul.loc['경기도']
sr_one.head(3)
sr_one.index
sr_one.values


# In[38]:


plt.plot(sr_one.index, sr_one.values)
plt.show()


# In[33]:


import platform
if platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic') 
elif platform.system() == 'Windows': #윈도우
        plt.rc('font', family='Malgun Gothic') 
elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
        plt.rc('font', family='Malgun Gothic') 

plt.rcParams['axes.unicode_minus'] = False #한글 폰트 사용시 마이너스 폰트 깨짐 해결


# In[52]:


plt.figure(figsize=(15,5))  # 그래프 사이즈 지정
plt.plot(sr_one.index, sr_one.values, marker='v', markersize=10, color='g')
plt.xticks(size=10, rotation='vertical')  # x축의 데이터를 세로로 회전
plt.title("서울에서 경기도로 이전한 인구수",size=20)  # 그래프의 제목
plt.xlabel('연도', size=20)  # x축 제목
plt.ylabel('이동 인구 수', size=20)  # y 축 제목
plt.legend(labels=["서울 -> 경기도"], loc='best', fontsize=13)


# In[54]:


# annotate 추가
plt.ylim(50000, 800000)
plt.annotate('',
            xy=(20,620000),     #  화살표 시작점
            xytext=(2,290000),  # 화살표 끝점
            xycoords='data',
            arrowprops=dict(arrowstyle='->', color='red', lw=3))
plt.annotate('인구 이동 증가(1970 - 1995)',
             xy=(10,380000),  # x좌표 y 좌표
             rotation=22,
             va='baseline',  # center, top, bottom, baseline
             ha='center',   # center, left, right
             fontsize=14)
plt.show()


# In[55]:


# 서울에서 제주도로 이동한 인구수만 검색해서 그래프로 나타내 보세요
sr_jeju = df_seoul.loc['제주특별자치도']
sr_jeju


# In[56]:


plt.figure(figsize=(15,5))  # 그래프 사이즈 지정
plt.plot(sr_jeju.index, sr_jeju.values, marker='v', markersize=10, color='g')
plt.xticks(size=10, rotation='vertical')  # x축의 데이터를 세로로 회전
plt.title("서울에서 ,제주도로 이전한 인구수",size=20)  # 그래프의 제목
plt.xlabel('연도', size=20)  # x축 제목
plt.ylabel('이동 인구 수', size=20)  # y 축 제목
plt.legend(labels=["서울 -> 제주도"], loc='best', fontsize=13)
plt.show()


# In[57]:


# 서울 -> 경기도  : sr_one
# 서울 -> 제주로 : sr_jeju 이동한 인구수의 그래프를 동시에 표현
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

# ax1 에 서울 -> 경기도  : sr_one
ax1.plot(sr_one, marker='o',color='b', markersize=10, label='서울 -> 경기')
ax2.plot(sr_jeju, marker='v',color='r', markersize=10, label='서울 -> 제주')
ax1.set_title('서울 경기 인구 이동')
ax2.set_title('서울 제주 인구 이동')
ax1.legend(loc='best')
ax2.legend(loc='best')

# y축 범위 (최소값, 최대값)
ax1.set_ylim(50000, 800000)
# ax2.set_ylim(50000, 800000)

ax1.set_xticks(sr_one.index)
ax2.set_xticks(sr_jeju.index)
# x축 연도 라벨 지정 -> 75도 기울여서
ax1.set_xticklabels(sr_one.index, rotation=45)
ax2.set_xticklabels(sr_jeju.index, rotation=45)

# 눈금 라벨 크기
ax1.tick_params(axis='x', labelsize=10)
ax2.tick_params(axis='y', labelsize=10)

plt.show()


# In[58]:


# 하나의 axes에 여러 개의 그래프를 추가로 그림
#  충청남도, 경상북도, 강원도, 1970 ~ 2017년 까지의 자료만 검색
col_years = list(map(str, range(1970,2018)))
col_years
df_1 = df_seoul.loc[['충청남도','경상북도','강원도'], col_years]
df_1


# In[59]:


fig = plt.figure(figsize=(20,5))
ax = fig.add_subplot(1,1,1)

ax.plot(col_years, df_1.loc['충청남도', :], marker='o', markerfacecolor='g',
       color='olive', label='서울->충남')
ax.plot(col_years, df_1.loc['경상북도', :], marker='o', markerfacecolor='b',
       color='skyblue', label='서울->경북')
ax.plot(col_years, df_1.loc['강원도', :], marker='o', markerfacecolor='r',
       color='r', label='서울->강원')
ax.legend(loc='best')
ax.set_title('서울->충남,경북,강원 인구 이동')
ax.set_xlabel('기 간')
ax.set_ylabel('인구 이동 수')

ax.set_xticks(col_years)
ax.set_xticklabels(col_years, rotation=75)

plt.show()


# In[60]:


# df_seoul.index
# 전라남도, 충청남도, 경상남도, 경기도로 이동한 인구수를
# 1. 하나의 화면에 모두 그리세요
df_2 = df_seoul.loc[['전라남도','충청남도','경상남도','경기도'], col_years]
df_2.head()


# In[61]:


fig = plt.figure(figsize=(20,5))
ax = fig.add_subplot(1,1,1)

ax.plot(col_years, df_2.loc['전라남도', :], marker='o', markerfacecolor='g',
       color='olive', label='서울->전남')
ax.plot(col_years, df_2.loc['충청남도', :], marker='o', markerfacecolor='b',
       color='skyblue', label='서울->충남')
ax.plot(col_years, df_2.loc['경상남도', :], marker='o', markerfacecolor='r',
       color='r', label='서울->경남')
ax.plot(col_years, df_2.loc['경기도', :], marker='o', markerfacecolor='y',
       color='y', label='서울->경기')
ax.legend(loc='best')
ax.set_title('서울->전남,충남,경남,경기 인구 이동')
ax.set_xlabel('기 간')
ax.set_ylabel('인구 이동 수')
ax.set_xticks(col_years)
ax.set_xticklabels(col_years, rotation=75)

plt.show()


# In[62]:


# 2. 화면을 4개로 분할해서 그래프를 그리세요
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

# ax1 에 서울 -> 전남  : sr_one
ax1.plot(df_2.loc['전라남도',col_years], color='b', label='서울->전남')
ax2.plot(df_2.loc['충청남도',col_years],color='r',label='서울->충남')
ax3.plot(df_2.loc['경상남도',col_years], color='y', label='서울->경남')
ax4.plot(df_2.loc['경기도',col_years],label='서울->경기')
ax1.set_title('서울 -> 전남 인구 이동')
ax2.set_title('서울 -> 충남 인구 이동')
ax3.set_title('서울 -> 경남 인구 이동')
ax4.set_title('서울 -> 경기 인구 이동')
ax1.legend(loc='best')
ax2.legend(loc='best')
ax3.legend(loc='best')
ax4.legend(loc='best')

# y축 범위 (최소값, 최대값)
ax1.set_ylim(10000, 100000)
ax2.set_ylim(10000, 100000)
ax3.set_ylim(10000, 100000)
ax4.set_ylim(50000, 800000)

# x축 정의
ax1.set_xticks(col_years)
ax2.set_xticks(col_years)
ax3.set_xticks(col_years)
ax4.set_xticks(col_years)

# x축 연도 라벨 지정 -> 75도 기울여서
ax1.set_xticklabels(col_years, rotation=90)
ax2.set_xticklabels(col_years, rotation=90)
ax3.set_xticklabels(col_years, rotation=90)
ax4.set_xticklabels(col_years, rotation=90)

plt.show()


# In[76]:


df_3 = df_2.T
df_3


# In[77]:


df_3.index = df_3.index.map(int)
df_3.index


# In[78]:


ax = df_3.plot(kind='area', figsize=(20,10))
ax.set_title('서울 -> 타 도시 인구 이동수')
ax.set_ylabel('이동 인구 수')
ax.set_xlabel('기 간')
ax.legend(loc='best', fontsize=16)

plt.show


# In[79]:


# 히스토그램
col_years = list(map(str, range(2010,2018)))
df_2 = df_seoul.loc[['전라남도','충청남도','경상남도','강원도'], col_years]
df_3 = df_2.T
df_3.index = df_3.index.map(int)


# In[80]:


ax = df_3.plot(kind='bar', figsize=(20,10))
ax.set_title('서울 -> 타 도시 인구 이동수', size=20)
ax.set_ylabel('이동 인구 수')
ax.set_xlabel('기 간')
ax.legend(loc='best', fontsize=16)

plt.show()


# In[81]:


# 남북한 전력 발전량
df = pd.read_excel('dataset/남북한발전전력량.xlsx')
df.head(10)

# 북한의 자료만 가져 옴 수력, 화력 발전량을 분석
df = df.loc[5:9]  # 5부터 8까지  
df.columns

# 전력량 (억㎾h) 컬럼을 삭제
df.drop('전력량 (억㎾h)', axis='columns', inplace=True)


# In[82]:


# 발전전력별 컬럼을 인덱스로 지정
df.columns
df.set_index('발전 전력별', inplace=True)

df = df.T

# 년도별로 증감율,  '합계' 컬럼명을 '총발전량'으로 변경
df = df.rename(columns={'합계':'총발전량'})

# 총발전량 - 1년 -> 이전 년도의 총발전량
df['총발전량 - 1년'] = df['총발전량'].shift(1)

# 증감율  (총발전량 / 이전 년도의발전량 - 1) * 100
df['증감율'] = ((df['총발전량']/df['총발전량 - 1년'])-1)*100
df


# In[83]:


# 그래프 그리기 : 수력, 화력 -> 증감율
ax1 = df[['수력', '화력']].plot(kind='bar',figsize=(20,10), stacked=True)
ax2 = ax1.twinx()

ax2.plot(df.index, df['증감율'], ls='--', marker='o', color='red',
        label='전년대비 증감율(%)')
ax1.set_ylim(0,500)
ax2.set_ylim(-50,50)

ax1.set_xlabel('연도', size=20)
ax1.set_ylabel('발전량(억 Kwh)')
ax2.set_ylabel('전년 대비 증감율 (%)')

plt.title('북한 전력 발전량')
ax1.legend(loc='best')

plt.show()


# In[84]:


df['총발전량'].shift(1)


# In[ ]:




