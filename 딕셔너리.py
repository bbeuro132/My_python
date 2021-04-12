#!/usr/bin/env python
# coding: utf-8

# In[7]:


bierce = {
    "day" : "A period of twenty=four hours, mostly misspent",
    "positive" : "Mistaken at the top of one's voice",
    "misfortune" : "The kind of fortune that never misses"
}

print(bierce["day"])


# In[9]:


lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
dict(lol)
# = {'a': 'b', 'c': 'd', 'e': 'f'}

lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
dict(lot)


# In[14]:


los = ['Ab', 'cd', 'ef']
dict(los)


# In[27]:


pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Gilliam': 'Terry'
}

pythons['Gilliam'] = 'Gerry'
pythons['Gilliam'] = 'Serry'


print(pythons.get('Gilliams'))
#get으로 키를 검색하면 에러를 일으키지 않는다.
#찾는 값이 없을 시에는 None을 출력한다.


# In[31]:


signals = {'green': 'go', 'yellow':'go faster', 'red':'smile for the camera'}
signals.keys()

list(signals.values())

list(signals.items())

len(signals)

