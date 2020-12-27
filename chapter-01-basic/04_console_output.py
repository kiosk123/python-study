# -*- coding: utf-8 -**
import math

# add : 9 sub = 2
print('add :', 4 + 5, 'sub =', 4 - 2)

# 1 2
# 3 4
print(1, 2); print(3, 4)

# 1 2 3 4
print(1, 2, end = ' '); print(3, 4)

# 1 2 3 4 5
print(1, 2, 3, 4, 5)

# 1,2,3,4,5
print(1, 2, 3, 4, 5, sep=",") 

# file 객체를 통해서 파일로 출력
f = open("./data/out.txt", 'w')
print(1, 2, 3, 4, 5, file = f)
f.close()

# 제곱근 출력
for k in range(1, 5):
    print('sqrt ({0})={1}'.format(k, math.sqrt(k)))
    

# 소수점 자리수를 3자리고 고정한 후 출력 {.을포함한 전체자릿수.소수점자리수f}
for k in range(1, 5):
    print('sqrt ({0})={1:5.3f}'.format(k, math.sqrt(k)))

# 키워드를 이용한 출력
print('나이:{age}, 키:{height}'.format(age = 19, height = 173))

# 사전을 이용한 출력. format_map사용 
print('나이:{age}, 키:{height}'.format_map({'age':19, 'height':173}))

# 이름 으로 접근하여 모듈의 값 출력
import sys
print('{0.float_info.max}'.format(sys))
    
# 데이터를 구조화하여 좀더 깔끔하게 출력
import pprint
complicated = ['spame', (1,2,3), ('ham', 'egg', ('ab', 'cd', ('abc', 'def')))]
complicated = complicated * 3
pprint.pprint(complicated)

'''
실행 결과
['spame',
 (1, 2, 3),
 ('ham', 'egg', ('ab', 'cd', ('abc', 'def'))),
 'spame',
 (1, 2, 3),
 ('ham', 'egg', ('ab', 'cd', ('abc', 'def'))),
 'spame',
 (1, 2, 3),
 ('ham', 'egg', ('ab', 'cd', ('abc', 'def')))]
'''
    