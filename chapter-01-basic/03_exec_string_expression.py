# -*- coding: utf-8 -*

num1 = 3
result = eval('num1 + 4') # 파이썬 표현식 실행
print(result) # 7

num2 = 5
exec('result = num2 + 4') # 문자열로 표현된 구문 실행
print(result) #9

flag = None
exp_str = '''
if result > 7:
    flag = True
else:
    flag = False
'''
exec(exp_str)
print(flag) # True

# 특정 문자열을 컴파일 코드로 한번 변환하고서 생성된 코드만 반복실행하여 실행시간 단축
# compile(source, filename, mode)
# source - 실행구문
# filename - 코드 문자열이 저장된 파일명 파일이아니라면 <string>사용
# mode - 어떤 종류의 코드가 컴파일되어야하는지 지정 하나의 문이면 single, 하나의 식은 eval, 여러개의 문은 exec 
code = compile('result + 1', '<string>', 'eval') 
result = 12
result = eval(code)
print(result) # 13

# 파일을 이용한 코드 실행
import os
a = None # src.py에서 사용하는 변수
filename = os.path.dirname(__file__) + '/data/src.py'
file = open(filename)
source = file.read()
code = compile(source, 'src.py', 'exec');
exec(code)
print(a)
file.close()

