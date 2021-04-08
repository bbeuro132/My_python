num1 = 3
num2 = 4
print(type(num1))
print('덧셈 :', num1+num2)
print('곱셈 :', num1*num2)
print('나머지 :', num1%num2)

res = num1 + num2
print('res : ', res)

res += num1

print('res : ', res)


# 비교 연산자
print(num1 > num2)
print(num1 < num2)

# 논리 연산자
print(num1 > num2 and num1 < num2)
print(num1 > num2 or num1 < num2)
print(not(num1 > num2))

# 3항 연산자
result = (num1 > num2) and \
    'num1이 num2보다 크다' or \
    'num1이 num2보다 작다'
print(result)

# 문자열
str1 = '홍길동'
str2 = '입니다.'
fullstr = str1 + str2
print(str1+str2)
print('문자열 연결 : ', fullstr)
fullstr = fullstr + '\n' + '안녕하세요.'
print('개행문자 :', fullstr)


# 문자열 인덱싱(indexing)
# 배열과 비슷함
print(str1[0], str1[1], str1[2])

# 문자열 자르기(slicing)

print(fullstr[0:2]) # 0 ~ 1까지 자르기 
print(fullstr[1:]) # 1 ~ 끝까지
print(fullstr[:3]) # 처음부터 ~ 2까지

print('\n\n' + fullstr[1::2]) # 1부터 끝까지 2번째 위치만


#in 연산자
search = '홍길동' in fullstr
print('\n', search)

length = len(fullstr)
print('변수값 크기 : ', length)