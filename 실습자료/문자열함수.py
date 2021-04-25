#!/usr/bin/env python
# coding: utf-8

# In[12]:


letters = ['yeti', 'bigfoot', 'Loch ness monster']
letters = '... '.join(letters)
print(letters)


# In[31]:


letters = 'WoRld'

letters.swapcase()


# In[35]:


a = '%s' % 42
b = '%d' % 30
print(type(a))
print(type(b))


# In[38]:


actor = 'Richard Gere'
cat = 'Chester'
weight = 28

a = "My wife's favorite actor is %s" % actor

b = "Our cat %s weight is %s pounds" % (cat, weight)

print(a)
print(b)


# In[43]:


'The {thing} is in the {place}'.format(thing='duck', place='bathtub')

thing = 'woodchuck'
place = 'lake'
'the {} is in the {}.'.format(thing, place)

'The {1} is in the {0}.'.format(place, thing)

d = {'thing' : 'duck', 'place' : 'bathtub'}

'the {0[thing]} is in the {0[place]}.'.format(d)


# In[50]:


thing = 'wereduck'
place = 'werepond'

print(f'the {thing} is in the {place}\n')

print(f'the {thing.capitalize()} is in the {place.rjust(20)}\n')

print(f'the {thing:>20} is the the {place:.^20}\n')

print(f'{thing = }, {place = }\n')

print(f'{thing[-4:] = }, {place.title() = }\n')

print(f'{thing = :>4.4}')

