# -*- coding: utf-8 -*

n1 = 4 + 5j
n2 = 7 - 2j
n1 * n2 # 38 * 27j

# 복소수의 실수부만 취한다  
n1.real # 4.0

# 복소수의 허수부만 취한다  
n1.imag # 5.0

a = 3; b = 4
complex(a, b) # a가 실수부, b가 허수부

# n1의 켤레 복소수를 구한다 
n1.conjugate() # 4 - 5j

# cmath 모듈을 이용한 복수수 연산
import cmath
cmath.sin(0.1 + 0.2j) # (0.10183674942129743+0.20033016114881572j)
cmath.sqrt(-2) # 1.4142135623730951j
cmath.log(2j) # (0.6931471805599453+1.5707963267948966j)

# 오일러 공식을 적용
from math import e, pi, cos, sin

e ** (pi / 4 * 1j) # (0.7071067811865476+0.7071067811865476j)
complex(cos(pi / 4), sin(pi / 4)) # 위와 동일

