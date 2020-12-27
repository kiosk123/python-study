# -*- coding: utf-8 -*
from sys import byteorder

n = 10 # 10진수
p = type(n) # n의 타입확인
print(p) # <class 'int'>

p = isinstance(n, int) #n이 int 타입인지 확인
print(p) # True

p = 0o23 # 8진수
print(p) # 19

p = 0x23 # 16진수
print(p) # 35

p = 0b1101 # 0b로 시작하면 2진수
print(p) # 13

p = 2 ** 1024
print(p) # 정수형 표현범위에 제한없음

l = p.bit_length() # 2 ** 1024를 표현하는데 필요한 비트 길이를 구한다
print(l) # 1025

bin(23) # 10진수 23을 2진수로 변환
oct(23) # 10진수 23을 8진수로 변환
hex(23) # 10진수 23을 16진수로 변환

int(2.9) # 소수점 2.9로 정수 2를 얻음 뒷자리는 버려짐
int(-2.9) # -2
int('123') # 문자열 123을 정수 123으로 변환

try:
    int('123.25') # 오류 발생
except ValueError:
    pass

try:
    int(2 + 3j) # 복소수 형도 정수형으로 변환안됨
except TypeError as e:
    print(e) # can't convert complex to int
    pass

float(123) # 정수형을 소수로 변환 123.0
str(123) # 정수형을 문자 '123'으로 변환
complex(123) # 정수를 복소수형으로 변환 123+0j

# 정수형 데이터를 직접 바이트 열로 변환
n = 1024
r = n.to_bytes(2, byteorder = 'big') # 2바이트를 빅엔디안으로 변환
print(r) # b'\x04\x00'

r = n.to_bytes(2, byteorder = 'little') # 2바이트를 리틀엔디안으로 변환
print(r) # b'\x00\x04'

n = -1024
r = n.to_bytes(4, byteorder = 'big', signed = True) # Signed는 부호비트를 설정
print(r) # b'\xff\xff\xfc\x00'


# 바이트 열에서 정수형으로 변환
r = int.from_bytes(b'\x04\x00', byteorder = 'big')
print(r) # 1024

r = int.from_bytes(b'\x00\x04', byteorder = 'little')
print(r) # 1024

r = int.from_bytes( b'\xff\xff\xfc\x00', byteorder = 'big')
print(r) # 4294966272

r = int.from_bytes( b'\xff\xff\xfc\x00', byteorder = 'big', signed = True) # Signed는 부호비트를 설정
print(r) # b'\xff\xff\xfc\x00'