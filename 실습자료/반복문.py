#!/usr/bin/env python
# coding: utf-8

# In[ ]:


count = 1
while count <= 5:
    print(count)
    count+=1


# In[ ]:


while True :
    stuff = input("String to capitalize [type q to quit] : ")
    if stuff == "q":
        break
    print(stuff.capitalize())


# In[ ]:


while True:
    value = input("Integer, please [q to quit] : ")
    if value == 'q' :
        break
    number = int(value)
    if number % 2 == 0 :
        continue
        
    print(number, "squared is", number*number)


# In[ ]:


word = 'thud'
for letter in word:
    if letter == 'x':
        print("Eek! An 'x'!")
        break
    print(letter)
else:
    print("No 'x' in there.")


# In[ ]:


numbers = [1,3,5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0 :
        print('Found even number', number)    
        break
    position += 1
else : 
    print('No even number found')


# In[ ]:


word = 'thud'
for letter in word:
    if letter == 'x':
        print("Eek! An 'x'!")
        break
    print(letter)
else:
    print("No 'x' in there.")


# In[ ]:


bucket = ['딸기', '수박', '사과', '참외']

for fruit in bucket :
    print(fruit)


# In[ ]:


List = [3,2,1,0]
for lst in List :
    print(lst)


# In[5]:


guess_me = 7
number = 5

while True :
    if number < guess_me :
        print('too low')
    if number == guess_me :
        print('found it!')
        break
    number+=1
    if number > guess_me :
        print('opps')
        break


# In[13]:


dan = int(input('몇 단을 출력하나요 : '))
for i in range(1,dan+1) :
    for j in range(1, 10) :
        print('%d x %d = %d'% (i, j, i*j))
    print('\n')


# In[17]:


guess_me = 5

for number in range(1, 10):
    if number < guess_me :
        print('too low')
    if number == guess_me :
        print('found it!')
        break
    if number > guess_me :
        print('opps')
        break

