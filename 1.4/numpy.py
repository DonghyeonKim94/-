#!/usr/bin/env python
# coding: utf-8

# In[1]:


# numpy 관련
import numpy as np


# In[2]:


arr = np.arange(15)


# In[8]:


arr


# In[15]:


type(arr)
arr = np.arange(18)
print(arr, type(arr))  #array
arr.reshape(3,6)  #reshape : 배열 재정의
print(arr, arr.ndim)   # ndim 몇차원인가
print(arr.shape, arr.size, arr.dtype.name)  # shape(3*5)
print(arr.itemsize)   # 데이터의 저장 공간 : 4 byte


# In[5]:


a_list = list(range(15))
a_list


# In[6]:


type(a_list)


# In[23]:


arr = np.arange(-5, 5, 0.5)
print(arr.size)
print(arr)
arr1 = arr.flatten()  # 다차원을 1차원으로 변형
arr1.ndim # 차원 알아보는함수


# In[26]:


# 기존의 파이썬 리스트로 array 생성
list_a = np.array([1,2,3])
list_b = np.array([[1,2,3], [4,5,6]])
print("list_a : {}, list_a 의 type : {}".format(list_a, type(list_a)))
print("list_b : {}, list_b 의 type : {}".format(list_b, type(list_b)))
print("list_a dim : {}, list_a 의 shape : {}".format(list_a.ndim, list_a.shape))
print("list_b dim : {}, list_b 의 shape : {}".format(list_b.ndim, list_b.shape))
print("list_a 의 size {}, list_a 의 dtype {}".format(list_a.size, list_a.dtype))


# In[ ]:


#np.arange([start], stop, [step])
#np.array.reshape(차수, ..), np.flatten() -> 1차원으로 변경
#np.ndim, np.shape, np.dtype, np.dtype.name, np.size

