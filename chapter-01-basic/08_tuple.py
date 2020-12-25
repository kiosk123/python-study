# -*- coding: utf-8 -*
'''
튜플은 리스트와는 다르게 값을 변경할 수 없다
'''
t = (1, 2, 3)
value = len(t) # 데이터 갯수 구하기

value = t[0] #인덱싱
value = t[-1]

value = t[0:2]
value = t[::2]

t = t + t + t 
print(t) # (1, 2, 3, 1, 2, 3, 1, 2, 3)

t = (1, 2, 3)
t = t * 3
print(t) # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 특정 값이 튜플에 속에 있는지 검사
value = 3 in t
print(value) # True

