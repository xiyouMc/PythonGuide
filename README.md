# PythonGuide
This`s a guide of python.
[中文说明](https://github.com/xiyouMc/PythonGuide/wiki)
```python
import json
data = {'b':123,'c':456,'a':'789'}

d1 = json.dumps(data,sort_keys=True,indent=4);

print d1
print data


print '''line1
line2
line3'''

print 3>2

print True and False

print not True

age = 17
if age >18:
    print 'adult'
else:
    print 'teenager'
PI=1111
print PI
print 10.0/3
#list
classmates=['Mark','Bob','Tracy']
print classmates

# list len
print len(classmates)
print classmates[0]

# last
print classmates[-1]
classmates.append("Adam")
print classmates
classmates.insert(1,'aaaa')
print classmates
classmates.pop();
print classmates

#tuple Not Change.diff list:not append insert
noChange=('aa','bb')
print noChange

t = (1,)
print t

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print L[0][0]
print L[1][1]
print L[2][2]

#if...elif
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
s = '123'
birth = int(s)
if birth<200:
    print 'AAA'
else:
    print 'BBB'

#for in
names=['Mark','Bob','Tracy']
for name in names:
    print name

# 1+2....+1000 range
sum=0
for x in range(1000):
    sum = sum + x
print sum

n = 0
while n < len(L):
    i = 0
    while i < len(L[n]):
        print L[n][i]
        i = 1+i
    n = 1+n
#dict->Map
d = {'Mark':95,'Bob':75,'Tracy':85}
print d['Mark']
d.pop('Tracy')
print d

```

http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000
