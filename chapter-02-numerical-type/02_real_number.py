# -*- coding: utf-8 -*
# 실수는 8바이트로 표현 

n = 1.2
p = type(n)
print(p) # <class 'float'>

isinstance(n, float) # True

p = 3e3 # 지수를 포함한 실수표현 3 곱하기 10의 3승과 동일
print(p) # 3000.0

p = -0.2e-4
print(p) # -2e-05 지수부는 정수일 수 있으나 실 수 있는 없다

import sys

# 실수로 표현 할 수 있는 최대값 : 1.7976931348623157e+308 
print(sys.float_info.max)

# 실수로 표현 할 수 있는 최소값 : 2.2250738585072014e-308
print(sys.float_info.min)

# 무한대 표현
float('inf')
float('-inf')

inf = float('inf')
result = inf / 10000
print(result) # inf

# 실수형 값이 정수로 오차없이 표현할 수 있는 값인지 여부를 판단
n = 1.2
n.is_integer() # False

n = 1.0
n.is_integer() # True

# 반올림
round(1.2) # 1
round(1.8) # 2

import math
math.ceil(1.2) # 2
math.floor(1.9) # 1


