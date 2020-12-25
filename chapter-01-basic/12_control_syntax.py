# -*- coding: utf-8 -*

# if 문
value = 10
if value > 10:
    print("value gt 10")
elif value == 10:
    print("value eq 10")
else:
    print("value lt 10")
    
# 삼항 연산자 value > 30보다 크면 value * 10실행 아니면 value /2 실행
x = (value * 10) if value > 30 else value / 2
print(x) # 5.0

# for문
for i in range(10):
    print(i, end=' ') 
print() 

# for문의 else블록은 beak문으로 중단되지 않았을 때실행
for i in range(10):
    print(i, end=' ')
else:
    print("\ncomplete") 
print("done")

# else문 실행 안됨
for i in range(10):
    print(i, end=' ')
    if i == 5:
        break
else:
    print("\ncomplete") 
print("\ndone")


# while문
value = 0
while value < 10:
    value += 1
print(value)

# 마찬가지로 break 사용시 else 실행안딤
value = 0
while value < 10:
    value += 1
    if value == 5: break
else:
    print("complete while loop")
    
    
# with문
# open()-close()와 save()-restore()같은 두개의 관련된 연산들 사이에서 작업을 자동화 할때 사용
# 파일 객체를 with를 이용하여 수행할때 close() 따로 호출 안해도됨
with open('./data/with.txt', 'w') as f:
    for i in range(100):
        f.write(str(i) + "\n")

# try-except 예외처리에 사용한다
try:
    s = 'abcd'
    int(s)
except Exception as e:
    print(type(e)) # ValueError
    print(e) # invalid literal for int() with base 10: 'abcd'