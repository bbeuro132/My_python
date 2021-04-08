#!/usr/bin/env python
# coding: utf-8

# In[27]:


import random

rand = random.randrange(1, 999)

while True :
    input1 = int(input('숫자 입력 : '))
    if input1 == rand :
        print('정답입니다.')
        break
    elif input1 > rand :
        print('보다 작은 수입니다.')
    elif input1 < rand :
        print('보다 큰 수입니다.')
    

