# -*- coding: utf-8 -*

# 사전 초기화 방법
d = {'one':'하나','two':'둘','three':'셋'}
d2 = dict(one = '하나', two = '둘', three = '셋')

value = d['one']; print(value) # 하나
d['four'] = '넷' # 사전에 항목 추가

d['one'] = 1 # 기존 값 변경

# 특정 키를 참조하는 항목이 있는지 여부
value = 'one' in d ; print(value) # True

# 키만 추출 dict_keys(['one', 'two', 'three', 'four'])
keys = d.keys(); print(keys) 
for key in keys:
    print(key)
    
# 값만 추출
values = d.values()
print(values) # dict_values([1, '둘', '셋', '넷'])

for value in values:
    print(value)
    
# (키, 값) 형태의 튜플로 변환
tuples = d.items()
print(tuples) # dict_items([('one', 1), ('two', '둘'), ('three', '셋'), ('four', '넷')])

for t in tuples:
    print(t)
