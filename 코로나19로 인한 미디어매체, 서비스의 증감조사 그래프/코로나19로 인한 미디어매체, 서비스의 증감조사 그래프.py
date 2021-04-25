#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

service = pd.read_csv('한국언론진흥재단_코로나19이후국민의일상변화조사_코로나19 이후 미디어서비스 이용량 변화_20201231.csv', header=None, encoding = 'cp949', skiprows=1)
contents = pd.read_csv('한국언론진흥재단_코로나19이후국민의일상변화조사_코로나19 이후 미디어콘텐츠 이용량 변화_20201231.csv', header=None, encoding = 'cp949', skiprows=1)

serv = ['OTT 서비스', '포털', '1인 미디어', '종편 보도', '메신저', '지상파', '소셜미디어', '뉴스', '예능', '드라마', '게임', '시사교양', '영화', '스포츠', '애니메이션']

array = []
Bool = True
num = 0
index = np.arange(len(serv))
fusion = pd.concat( [service, contents], axis = 0)
numbers = np.zeros((15, 4))

del fusion[0]

for i in range(15):
    for j in range(4):
        numbers[i][j] = fusion.to_numpy()[i][j]
        
for i in numbers:
    array.append(i)

plt.title('코로나19로 인한 매체 이용량 증감 그래프')
plt.rcParams['figure.figsize'] = (20, 7)
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['lines.linewidth'] = 5

plt.xticks(index, serv)
plt.xticks(rotation=20)
plt.ylim([0, 80])

for i in range(15):
    plt.bar(index[num]-0.3, array[num][1], width=0.3, color="g", label = '증가')
    plt.bar(index[num], array[num][3], width=0.3, color="salmon", label = '변화 없음')
    plt.bar(index[num]+0.3, array[num][2], width=0.3, color="b", label = '감소')
    if Bool == True:
        plt.legend()
        Bool = False
    num+=1

plt.show()

