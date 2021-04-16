#!/usr/bin/env python
# coding: utf-8

# In[203]:


from matplotlib import pyplot
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker #눈금 표시를 위한 라이브러리


address = ['서울', '경기', '부산', '대구', '대전', '광주', '충청', '전라', '경상', '강원', '제주', '세종', '인천', '울산']
#서울, 경기, 부산, 대구, 대전, 광주, 충청, 전라, 경상, 강원, 제주, 세종, 인천, 울산
file = open('210416.csv', encoding = 'cp949')

data = csv.reader(file)

seoul= gyeongi = busan = daegu = daegeon = gwangju = chungcheong = geonla = gyeongsang = gangwon = jeju = 0
sejong = incheon = ulsan = 0

for i in data :
    if address[0] in i[6]:
        seoul+=1
    elif address[1] in i[6]:
        gyeongi +=1
    elif address[2] in i[6]:
        busan += 1
    elif address[3] in i[6]:
        daegu += 1
    elif address[4] in i[6]:
        daegeon += 1
    elif address[5] in i[6]:
        gwangju += 1
    elif address[6] in i[6]:
        chungcheong += 1
    elif address[7] in i[6]:
        geonla += 1        
    elif address[8] in i[6]:
        gyeongsang += 1    
    elif address[9] in i[6]:
        gangwon += 1
    elif address[10] in i[6]:
        jeju += 1
    elif address[11] in i[6]:
        sejong += 1
    elif address[12] in i[6]:
        incheon += 1
    elif address[13] in i[6]:
        ulsan += 1
        
file.close()

values = [seoul, gyeongi, busan, daegu, daegeon, gwangju, chungcheong, geonla, gyeongsang, gangwon, jeju, sejong, incheon, ulsan]
local = address 
# local에 address를 대입


ax = plt.axes()

x = np.arange(14) # X축의 범위는 14개로 지정4개로 지정



plt.xticks(x, local)
# X축을 나누는 기준은 local에 담긴 값

plt.ylim([0, 30]) # Y축 범위는 0부터 30

plt.rcParams['font.size'] = 17
plt.rcParams['font.family'] = 'NanumGothic'# 폰트는 나눔고딕

plt.bar(x, values, width=0.6, color="salmon", edgecolor="white", linewidth=2) # 디자인

ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))# 한칸마다 보조눈금을 그린다

plt.grid(which='major', linewidth = '0.9', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')

pyplot.rcParams["figure.figsize"] = (15,11)
plt.tick_params(axis='y', direction='in', length = 10, pad = 10, labelsize=20, width = 2, color='black')



plt.title('지역별 접종센터 개수', color='k')



plt.show()


# In[91]:


a = b = 0

