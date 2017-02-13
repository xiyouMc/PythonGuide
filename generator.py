# -*- coding:utf-8 -*-
from collections import Iterable
from collections import Iterator
g = (x* x for x in range(100))
print g
for n in g:
    print n

#Fibonacci
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        print b
        a,b=b,a+b
        n = n+1
    return 'done'
#fib(6)

#yield
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n = n+1

a = fib(6)
for x in a:
    print(x)

#杨辉三角
def triangles(max):
    L=[1]
    n = 0
    while 1:
        yield L
        L = [L[x] + L[x +1] for x in range(len(L)-1)]
        L.insert(0,1)
        L.append(1)
        n = n+1
        if(n > max):
            break
for x in triangles(20):
    print x


print isinstance(iter('abc'), Iterator)

print isinstance((x for x in range(10)), Iterator)
