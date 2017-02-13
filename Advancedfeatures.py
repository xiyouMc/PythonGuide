from collections import Iterable
import os
#Slice
L=('Mark','Bob','Tracy')
print L[0:3],L[:3],L[-1]

L=range(1000)
print L[:10]
print L[-10:]
print L[:10:2]
print L[::10]

print 'ABCDEFG'[:3]
print 'ABCDEFG'[::2]
d={'a':1,'b':2,'c':3}
for key in d:
    print key
for k,v in d.items():
    print 'key:',k," value:",v

for ch in 'ABC':
    print(ch)
print isinstance(123,Iterable)
#List Comprehensions
print [x*x for x in range(1,11) if x%2 ==0]
print [m+n for m in 'ABC' for n in 'DEF']
print [d for d in os.listdir('.')]
d={'A':1,'B':2,'c':3}
print [k.lower() + '+' +str(v) for k,v in d.items()]
