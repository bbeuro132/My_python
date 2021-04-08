

# 변수를 사용해서 아래와 동일하게 출력
# -------------------
# 개인 주소록
# -------------------
# 1. 이름 : 홍길동
# 2. 성별 :
# 3. 나이 : 200살
# 4. 주소 : 조선 한양 홍대감댁 11번지
# 5. 취미 : 무술훈련


name = '홍길동'
gender = '남'
age = 200
address = '조선 한양 홍대감댁 11번지'
hobby = '무술훈련'

print('이름 : ', name)
print('성별 : ', gender)
print('나이 : ', age,'세')
print('주소 : ', address)
print('취미 : ', hobby)

print('\n이름:{0}, 성별:{1}, 나이:{2}'.format(name, gender, age))
print('\n이름:%s, 성별:%s, 나이:%d세'% (name, gender, age))


print(name, gender, age, address, sep='::')
print(name, gender, age, address, sep='//', end='!!')
# sep : 구분자, 변수 사이사이에 넣을 문자를 지정할 수 있음
# end : 출력문의 마지막에 삽입할 문구