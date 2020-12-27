# -*- coding: utf-8 -*
from Tools.pynche.Main import docstring
s = "Hello World!"

s[0]  # H
s[-1]  # !
s[1:3] #el
s[:] # 전체 출력 Hello World!
s[::2] # 두칸 단위로 문자 추출  HloWrd
s[::-1] # 거꾸로 출력 !dlroW olleH
s.upper() # 대문자 변환 HELLO WORLD!
s.split(" ") # 문자열 공백을 기준으로 분리 ['Hello', 'World!']
s.find('World') #문자열 위치 6
s.startswith("Hello") # 특정 문자열로 시작하는지 여부 True
s.endswith("World!") # 특정 문자열로 끝나는지 여부
len(s) # 문자열 길이 출력
'a' + 'b' #문자열 더하기 연산 ab
'a'*3 # 문자열 곱하기 연산 aaa
# 문자열이 숫자로만 구성되어 있는지 판별
'1234'.isnumeric() #True
'1234'.isdigit()

# 문자열이 유니코드 수치 혹은 일반 수치 문자인지
'123\u2155\u2156'.isnumeric() # True

# 일반 수치 혹은 유니코드 수치 문자인지
'123\u0661'.isdecimal() # True

# 문자열이 영문자 혹은 유니코드 문자인지
'abcd한글'.isalpha() # True

# 문자열이 숫자나 영문자 혹은 유니코드 문자인지
'1abc234'.isalnum() # True

# 문자열이 소문자 인지
'abc'.islower() # True

# 문자열이 대문자인지
'ABC'.isupper() # True

# 문자열이 공백문자인지
'\n\r\t'.isspace() # True

# 제목 문자열인지
'This is A Title'.istitle() # True

# 문자열이 예약어인지
'def'.isidentifier() # True

# 문자열이 인쇄 가능한 문자들인지
'\n\t'.isprintable() # False

# 5길이보다 작은 문자열의 자리를 0으로 채운다
s = '123'
s.zfill(5) # 00123

u = ' abc '
u.strip() # 좌우 공백 제거 후 출력
u.rstrip() # 오른쪽 공백 제거 후 출력
u.lstrip() # 왼쪽 공백 제거 후 출력

u = 'spam'

u.center(10) # 전체 10문자의 가운데 정렬 '   spam   '
u.center(10, '-') # 전체 10문자의 가운데 정렬 후 공백을 -로 채우기 ---spam---
u.ljust(10) # 왼쪽에 정렬
u.rjust(10) # 오른쪽에 정렬

'1\tand\t2'.expandtabs() # 탭문자를 공백문자로 변경
'1\tand\t2'.expandtabs(4) # 탭문자를 공백 4문자로 변경

# 문자열 매핑처리
instr = 'abcdef'
outstr = '123456'
tranref = ''.maketrans(instr, outstr)

'as soon as possible'.translate(tranref) # 1s soon 1s possi2l5

import math
'sqrt ({0})={1}'.format(10, math.sqrt(10)) # 뮨저욜 포매팅
    

# 소수점 자리수를 3자리고 고정{.을포함한 전체자릿수.소수점자리수f}
'sqrt ({0})={1:5.3f}'.format(10, math.sqrt(10))

# 키워드를 이용한 포매팅
'나이:{age}, 키:{height}'.format(age = 19, height = 173)

# 사전을 이용한 포매팅. format_map사용 
'나이:{age}, 키:{height}'.format_map({'age':19, 'height':173})
