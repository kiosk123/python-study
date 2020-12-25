# -*- coding: utf-8 -*

result = 4 + 5
print(result) #9

result = 12 -32
print(result) #

result = (4 + 5) * 6
print(result) 

result = 3 / 2 # 나누기 - 결과는 소수
print(result)  # 1.5

result = 3 // 2 # 몫만
print(result) 

result = 9 % 5 # 나머지
print(result) 

result = divmod(9, 5) # 나머지와 몫을 한꺼번에 계산
print(result)

# 복소수 연산
op1 = 1 + 4j
op2 = 5 - 3j
result = op1 * op2
print(result)

# cmath 모듈을 이용한 복소수 연산
from cmath import *
print(cos(pi / 3), sin(pi / 3)) # (0.5000000000000001-0j) (0.8660254037844386+0j)

result = sqrt(-2)
print(result) # 1.4142135623730951j

