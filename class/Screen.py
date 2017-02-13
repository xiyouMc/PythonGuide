#-*-coding:utf-8 -*-

class Screen(object):

    def __init__(self,name):
        self.name = name
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height = value

    #只读
    @property
    def resolution(self):
        return self._width * self._height

    #__str__可格式化对象的内容。 类似java 的toString()
    def __str__(self):
        return 'Student object (name:%s)' % self.name
    __repr__ = __str__
s = Screen('AA')
s._width = 1024
s._height = 768
print(s.resolution)
print(s)
s
#实现for...in循环
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):#实例本身就是迭代对象，故返回自己
        return self

    def nextr(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a >1000:
            raise StopIteration();
        return self.a;
for n in Fib():
    print n
