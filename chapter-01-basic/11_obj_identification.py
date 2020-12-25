# -*- coding: utf-8 -*

a = [1,2,3]
b = [1,2,3]

# a 와 b가 같은 객체를 참조하는지
r = a is b; print(r) # False

# a와 b의 객체의 값이 같은지
r = ( a == b ); print(r) # True