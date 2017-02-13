def my_abs(x):
    if x>0:
        return x
    else:
        return -x;
print my_abs(-10)


def power(x,n=2,a=1):
    s = 1
    while n >0:
        n = n-1
        s = s*x
        return s
print power(2)

print power(2,a=2)


def add_end(L=None):
    if L is None:
        L = []
    L.append('end')
    print L

add_end()

#a^2 + b^2 + c^3
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n;
    print sum

calc([1,3,5,7])

#*->can be Change
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n;
    print sum
calc(1,3,5,7)

# **
def calc(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
extra={'city':'Beijing','job':'Engineer'}
calc('Mark',23,**extra)
