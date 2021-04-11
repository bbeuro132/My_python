#!/usr/bin/env python
# coding: utf-8

# In[11]:


empty_tuple = (1,2,3)

print(empty_tuple)
print(type(empty_tuple))

one_marx = ('Groucho',)

print(one_marx)
print(type(one_marx))
print(type('Groucho',))

print(type(('Groucho',)))


# In[15]:


marx_tuple = ('Groucho', 'chico', 'harpo')
a,b,c = marx_tuple

alphabet = 'abcd'
number = '1234'

alphabet, number = '1234', 'abcd'

number


# In[26]:


temp_list = ['aaa', 'bbb', 'ccc']

print(temp_list)
print(type(temp_list))

temp_list = tuple(temp_list)

print('\n',temp_list)
print(type(temp_list))


# In[32]:


words = ('aaa', 'bbb', 'ccc', 'ddd')

for word in words :
    print(word)


# In[37]:


t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
print(id(t1))
t1+=t2

print(t1)
print(id(t1))


# In[11]:


'''append() : 리스트 끝에 항목 추가
insert() : 원하는 위치에 항목추가 가능
extend() : 리스트와 리스트를 병합할 때 사용

ex) numbers = [1,2,3,4]
numbers[1:3] = [8,9]
numbers = [1,8,9,4]

del 리스트이름[위치] : 특정 위치에 있는 항목 삭제
remove('값') : 특정 값을 지정하여 삭제(위치를 모를 때)
pop() : 지정한 위치의 값을 가져온 뒤 삭제
clear() : 모든 항목을 지우는 메서드

index('값') : 입력한 값의 위치를 알려주는 메서드
리스트이름 in '값' : 해당 값이 리스트 내부에 있는지 알려주는 메서드 '''

temp = ['a','b','c','d','e']

temp.append('F')

print(temp)

temp.insert(2, 'Q')

print(temp)


# In[16]:


temp = ['a','b','c','d','e']

temp[0] = 'Q'

print(temp)


# In[22]:


temp = ['a','b','c','d','e']
#temp.remove('a')
print(temp.pop(0))
print(temp)


# In[27]:


temp = ['a','b','c','d','e']
#temp.clear()

print(temp.index('d'))

'a' in temp


# In[34]:


friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)
print(type(joined))

separated = joined.split(separator)
print(separated)
print(separated == friends)
print(type(separated))


# In[41]:


temp = [3,4,6,2,1,8,6]
sorted_temp = sorted(temp)
print(sorted_temp)

print(temp)

temp.sort(reverse=True)
temp


# In[44]:


a = [1,2,3]
b = a.copy()
c = list(a)
d = a[:]
#b, c, d는 a의 복사본이다.

a[0] = 'integer lists are boring'
print(a)
print(b)
print(c)
print(d)

