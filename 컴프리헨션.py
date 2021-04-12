#!/usr/bin/env python
# coding: utf-8

# In[5]:


a = 'apple'
b = 'banana'

print(a+' '+b)
print(a,b)


# In[9]:


number_list = [number for number in range(1,6)]


a_list = []
for number in range(1,6):
    if number % 2 == 1:
        a_list.append(number)
        
a_list


# In[23]:


number_thing = (number for number in range(1,6))
print(number_thing)
num = number_thing

print(type(num))

for i in num:
    print(i)


# In[11]:


rows = range(1,4)
cols = range(1,3)
'''
for row in rows:
    for col in cols:
        print(row,col)
'''

cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

