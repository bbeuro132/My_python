print('hello 파이썬')
print('파이썬')
# 한줄 주석은 #를 쓴다.

'''
여러줄 주석
여러줄 주석
'''

'''
# 변수 선언 및 초기화
num = 10
str = '이원준'
print('문자열 str = ', str)
print('숫자 num = ', num)

print('숫자 num : %d'% num)
print('문자 str : %s'% str)

PI = 3.141592

print('실수 : %.2f'% PI)
'''

# 입력 처리
print('숫자 입력 : ')
input1 = input()
print(type(input1))

input2 = input('두 번째 숫자 입력 : ')
print(input2)


# 문자열 -> 숫자

# int() : 문자열 -> 숫자
# str() : 숫자 -> 문자열
sum = int(input1) + int(input2)
print('sum :',sum)

input3 = int(input('3번째 숫자 입력'))
print(type(input3))


