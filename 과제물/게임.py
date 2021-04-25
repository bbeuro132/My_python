#!/usr/bin/env python
# coding: utf-8

# In[11]:


import time

class player():
    def __init__(self, name, hp, atk, armor):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.armor = armor
    
class enemy():
    def __init__(self, name, hp, atk, armor):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.armor = armor
        
def play():
    p_name = input('플레이어 이름 : ')
    p_hp = int(input('플레이어의 체력 : '))
    p_atk = int(input('플레이어의 공격력 : '))
    p_def = int(input('플레이어의 방어력 : '))
    
    P = player(p_name, p_hp, p_atk, p_def)
    
    e_name = input('적의 이름 : ')
    e_hp = int(input('적의 체력 : '))
    e_atk = int(input('적의 공격력 : '))
    e_def = int(input('적의 방어력 : '))
    

    E = enemy(e_name, e_hp, e_atk, e_def)
    
    while True:   
        if E.hp > 0:
            if P.hp <= 0:
                print(P.name,'이(가) 쓰러졌습니다.')
                time.sleep(1)
                break 
 
            E.hp = (E.hp - P.atk) + E.armor
            print(P.name+'의 공격!',E.name+'의 남은 체력 :', E.hp)
            time.sleep(1)
            
        elif E.hp <= 0 : # 적의 체력이 0이거나 그 이하일 경우
            print(E.name+'이(가) 쓰러졌습니다.')
            break    
            
        if P.hp > 0:
            if E.hp <= 0:
                print(E.name,'이(가) 쓰러졌습니다.')
                time.sleep(1)
                break  
                
            P.hp = (P.hp - E.atk) + P.armor
            print(E.name+'의 공격!',P.name,'의 남은 체력 :', P.hp)
            time.sleep(1)
            
        elif P.hp <= 0 : #플레이어의 체력이 0이거나 그 이하일 경우
            print(P.name+'은(는) 쓰러졌습니다.')
            time.sleep(1)
            break    
    
    if P.hp > E.hp :
        print('플레이어의 승리!')
    if E.hp > P.hp :
        print('적의 승리...')
        
             
print('--------------------게임 시뮬레이터--------------------')     

play()


# In[ ]:


class Cat():
    def __init__(self, name, age, kind): # self.name은 this.name과 비슷하다고 볼수 있나?
        self.name = name
        self.age = age
        self.kind = kind
    def crying(self):
        return '애오옹'

furball = Cat('Grumpy', 3, 'munchkin') #생성자
cat2 = Cat('ann', 6, 'none')

print(furball.crying())


# In[ ]:


'''
# 초안
num = 0
Input = int(input('공격자는 누구인가요? 1.플레이어 2.적 : '))

if Input == 1 :
    time = int(input('몇 번 공격하나요? : '))    
    while num < time:
        if (E.hp > 0) :
            E.hp = (E.hp - P.atk) + E.armor
            print(P.name+'의 공격!',E.name+'의 남은 체력 :', E.hp)
            num+=1
    else :
        if (E.hp <= 0):
            print(E.name,'이(가) 쓰러졌습니다.')
        else :
            print(E.name,'은(는) 살아남았습니다.')
        
elif Input == 2 :
    time = int(input('몇 번 공격하나요 : '))
    while num <= time:
        if (P.hp > 0) :
            P.hp = (P.hp - E.atk) - P.armor
            print(E.name+'의 공격!',P.name,'의 남은 체력 :', P.hp)
            num+=1
    else :
        if (P.hp <= 0):
            print(P.name,'은(는) 쓰러졌습니다.')
        else :
            print(P.name,'은(는) 살아남았습니다. 다음을 기약하세요.')
'''
   

