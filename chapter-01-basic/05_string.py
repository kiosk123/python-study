# -*- coding: utf-8 -*
s = "Hello World!"

result = s[0] 
print(result) # H

result = s[-1] 
print(result) # !

result = s[1:3]
print(result) #el

result = s[:]
print(result) # 전체 출력 Hello World!

result = s[::2] # 두칸 단위로 문자 추출
print(result) # HloWrd

result = s[::-1] # 거꾸로 출력
print(result) # !dlroW olleH

result = s.upper() # 대문자 변환
print(result) # HELLO WORLD!

result = s.split(" ") # 문자열 공백을 기준으로 분리
print(result) # ['Hello', 'World!']

result = s.find('World') #문자열 위치
print(result) # 6

result = s.startswith("Hello") # 특정 문자열로 시작하는지 여부
print(result) # True

result = s.endswith("World!") # 특정 문자열로 끝나는지 여부
print(result)

result = len(s)
print(result) # 문자열 길이 출력

result = 'a' + 'b' #문자열 더하기 연산
print(result) # ab

result = 'a'*3 # 문자열 곱하기 연산
print(result) # aaa
