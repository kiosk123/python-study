# -*- coding: utf-8 -*
L = [1,2,3] #리스트 선언

value = L[0] #리스트 특정 인덱스 참조
value = L[-1]; print(value) #3
value = L[1:3]; print(value) # [2, 3]

value = L[::2]; print(value) # 2칸 단위로 슬라이싱 [1, 3]
value = L[::-1]; print(value) # 거꾸로 출력 [3, 2, 1]

L.append(4) # 리스트 마지막에 데이터 추가
print(L) # [1, 2, 3, 4]

del L[2] # 리스트내 데이터 삭제
print(L) # [1, 2, 4]

L.reverse() # 리스트의 순서를 바꿈
print(L) # [4, 2, 1]

L.sort() # 리스트를 오름차순으로 정렬
print(L) # [1, 2, 4]