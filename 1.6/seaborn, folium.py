#!/usr/bin/env python
# coding: utf-8

# In[24]:


import matplotlib.pyplot as plt

import platform
if platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic') 
elif platform.system() == 'Windows': #윈도우
        plt.rc('font', family='Malgun Gothic') 
elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
        plt.rc('font', family='Malgun Gothic') 

plt.rcParams['axes.unicode_minus'] = False #한글 폰트 사용시 마이너스 폰트 깨짐 해결


# In[25]:


import seaborn as sns


# In[26]:


titanic = sns.load_dataset('titanic')
print(titanic.head())
print()
titanic.info()


# In[27]:


# 회귀선이 있는 scatter 그래프, 회귀선이 없는 그래프를 그리려한다
sns.set_style('darkgrid')
fig = plt.figure(figsize=(15,6))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

sns.regplot(x='age', y='fare', 
           data=titanic,
           ax=ax1)
sns.regplot(x='age', y='fare', 
           data=titanic,
           ax=ax2,
           fit_reg=False)
plt.show()


# In[28]:


# 그래프 객체 생성 (figure에 3개의 서브 플롯을 생성)
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)
 
# distplot
sns.distplot(titanic['fare'], ax=ax1) 

# kdeplot
sns.kdeplot(x='fare', data=titanic, ax=ax2) 

# histplot
sns.histplot(x='fare', data=titanic,  ax=ax3)

# 차트 제목 표시
ax1.set_title('titanic fare - distplot')
ax2.set_title('titanic fare - kedplot')
ax3.set_title('titanic fare - histplot')

plt.show()


# In[30]:


import seaborn as sns

titanic = sns.load_dataset('titanic')

# heatmap
sns.set_style('darkgrid')
#피벗테이블로 범주형 변수를 각각 행, 열로 재구분하여 정리
table = titanic.pivot_table(index=['sex'], columns=['class'], aggfunc='size')

# 히트맵 그리기
sns.heatmap(table,                        #데이터프레임
           annot=True, fmt='d',          #데이터 값 표시 여부, 정수형 포맷  
           cmap='YlGnBu',                #컬러 맵
           linewidth=.5,                 #구분선
           cbar=False)                    #컬러바 표시여부
plt.show()


# In[41]:


# 지도 그래프
import folium # 서울 지도 만들기
import pandas as pd
seoul_map2 = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', 
                        zoom_start=12)
seoul_map3 = folium.Map(location=[37.55,126.98], tiles='Stamen Toner', 
                        zoom_start=15)

# 지도를 HTML 파일로 저장하기
seoul_map2.save('C:/Users/luis1/dataset/seoul2.html')
seoul_map3.save('C:/Users/luis1/dataset/seoul3.html')


# In[62]:


df = pd.read_excel("C:/Users/luis1/dataset/서울지역 대학교 위치.xlsx")

df
seoul_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain', zoom_start=12)

for name, lat, lng in zip(df.index, df.위도, df.경도):
    folium.Marker([lat, lng], popup=name).add_to(seoul_map)
    
seoul_map.save('C:/Users/luis1/dataset/seoul.html')


# In[63]:


#df.rename(index={'Unnamed:0':'name'}, axis='index', inplace=True)


# In[ ]:


df


# In[64]:


seoul_map = folium.Map(location=[37.55, 126.98], titles='Stamen Terrain', zoom_start=12)

for name, lat, lng in zip(df.index, df.위도, df.경도):
    folium.CircleMarker([])


# In[65]:





# In[ ]:




