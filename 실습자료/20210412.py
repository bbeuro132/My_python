#!/usr/bin/env python
# coding: utf-8

# In[12]:


#7.1 ~ 7.3 문제
year_list = []

year_list = [x for x in range(1996, 2002)]
    
print('출생 후 세 번째 생일은', year_list[3], '년이다.')

print('가장 나이가 많을 때는', year_list[-1], '년이다.')


# In[2]:


things = ['mozzarella', 'cinderella', 'salmonella']
#7.4

print(things[1].capitalize())
#7.5

print(things[0].upper())
#7.6


# In[3]:


surprise = ['Groucho', 'Chico', 'Harpo']
#7.8

s = surprise[2]
print(s[::-1].capitalize())
#7.9


# In[4]:


number_list = [number for number in range(1,10)]
List = []

for i in number_list :
    if i % 2 == 0 :
        List.append(i)

print(List)
#7.10


# In[13]:


start1 = ['fee', 'fie', 'foe']
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done")
]
start2 = "Someone better"

start1.append(rhymes[0][0])

List = []
num = 0

for i in start1:
    List.append(start1[num].title()+'!')
    num+=1

num = 0
for j in rhymes :
    print(' '.join(List))
    print(start2, rhymes[num][1]+'.')
    num+=1

