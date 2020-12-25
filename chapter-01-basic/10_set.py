# -*- coding: utf-8 -*
'''
중복없이 데이ㅓ를 저장한다.
'''
# 집합 추기화
s = {1, 2, 3}
s1 = set() # 공집합

L = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5]
s = set(L)
print(s) # {1, 2, 3, 4, 5}

# 집합안에 특정값이 있는지 판별
value = 3 in s ; print(value) # True

s = { 1, 2, 3 }
t = { 3, 4, 5, 6 }

r = s.union(t) # 합집합
print(r)  # {1, 2, 3, 4, 5, 6}

r = s.intersection(t) # 교집합
print(r) # {3}

r = s - t # 차잡합
r = s | t # 합집합
r = s & t # rywlqgkq

s.add(4) # 집합에 값 추가
print(s) # {1, 2, 3, 4}

s.discard(3) # 집합에서 값 제거
print(s) # {1, 2, 4}

