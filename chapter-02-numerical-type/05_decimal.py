# -*- coding: utf-8 -*
# 반복적인 산술연산시 시간이 걸리기 때문에  필요한 곳에서만 사용할 것

0.1 + 0.1 + 0.1 - 0.3 # 5.551115123125783e-17 오차 발생

from decimal import *

Decimal(1234) # 1234
Decimal('1234') # 1234

Decimal(1.1) # 1.100000000000000088817841970012523233890533447265625 오차 발생

# 오차 발생을 없애려면 문자로 생성한다
Decimal('1.1') # 1.1

Decimal('1.1') + Decimal('1.2') # 2.3 덧셈도 가능하다 

# 유효 자릿수 조정
getcontext().prec = 10
Decimal('2').sqrt() # 1.414213562

getcontext().prec = 20
Decimal('2').sqrt() # 1.4142135623730950488

# 미리 생성된 컨텍스트 객체를 통해서 유효자릿수 유효자리수와 소수점 올림 방식을 처리가능하다
ExtendedContext # prec 9, ROUND_HALF_EVEN
BasicContext # prec 9 ROUND_HALF_UP
DefaultContext # prec 28 ROUND_HALF_EVEN

# 설정은 setcontext()를 호출해서 설정을 변경한다.
setcontext(DefaultContext)
getcontext().prec = 20

Decimal(2).exp() # e^2 7.3890560989306502272

Decimal('10').ln() # log(10)
Decimal('10').log10() # log10(10)

# 언하는 소수점 자리의 수치 얻기

# .quantize 첫번째 파라미터는 자릿수를 결정하고 값은 의미없다 자릿수만 중요 
Decimal('7.329').quantize(Decimal('.01'), rounding = ROUND_DOWN) # 7.32 - 무조건 버림
Decimal('7.329').quantize(Decimal('.01'), rounding = ROUND_UP) # 7.33 - 무조건 올림
Decimal('7.329').quantize(Decimal('.01'), rounding = ROUND_HALF_UP) # 7.33 - 반올림

# 지수부 가수부를 별도 지정
Decimal((1, (1,4,7,5), -2)) # -14,75 첫번째 파라미터가 1이면 음수

# math 모듈과 함께 사용가능
import math
d = Decimal('123.456789012345')
math.sqrt(d)


# cmath 모듈과 함께 사용
import cmath
cmath.sqrt(-d)

