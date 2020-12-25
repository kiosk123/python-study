# -*- coding: utf-8 -*
'''
바이트와 문자열의 차이
s = '이강성' # 문자열은 유니코드를 기본
s = b'이강성' # 1바이트(0~255)로 표현되는 문자만 표현가능 - 에러발생
'''
b = b'Python rules' # 바이트 상수 선은은 b로 시작
print(b) # b'Python rules'

result = type(b) # b변수의 타입 출력
print(result)  # <class 'bytes'>

result = b.decode() # 바이트를 문자열로 표현 - 기본 인코딩은 UTF-8
print(result)

result = b.decode('euc-kr') # 바이트를 문자열로 표현 - euc-kr로 인코딩 지정
print(result)

result = '이강성'.encode() # 문자열을 바이트로 표현
print(result) # b'\xec\x9d\xb4\xea\xb0\x95\xec\x84\xb1'

# 변경가능한 바이트를 원하는 bytearray를 사용
ba = bytearray(b)
ba[7] = ord('R') # ord를 이용해 'R'을 유니코드 값으로 변경 후 bytearray에 값 설정
print(ba) # bytearray(b'Python Rules')

# bytearray를 다시 bytes(바이트)로 변환
b = bytes(ba)
print(b) # b'Python Rules'

# bytearray를 문자열로 변환
result = ba.decode()
print(result) # Python Rules