# -*- coding:utf-8 -*-
#继承
class Animal(object):
    __slots__ = ('name','age') # 用tuple定义允许绑定的属性名称
    def run(self):
        print('Animal is running....')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    pass
class Cat(Animal):

    def run(self):
        print('Cat is running...')
    pass

def run_twice(animal):
    animal.run();
dog = Dog();
dog.run()

run_twice(Animal())
run_twice(Dog())

print type(dog)
print dir(dog)

#绑定方法 只对当前示例生效
def set_age(self,age):
    self.age = age;
s = Dog();
from types import MethodType
s.set_age = MethodType(set_age,s);
s.set_age(25)
print s.age

#给所有实例绑定方法
Dog.set_age=set_age;
dogTest = Dog()
dogTest.set_age(22)
print dogTest.age

#__slots__限制绑定的属性名,子类不能被限制
catSlots = Animal();#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
catSlots.name = 'a'
catSlots.age = 12
#catSlots.score = 11;
#print catSlots.score


#property 可直接将方法变成属性来调用
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s = Student();
s.score = 60
print s.score
s.score = 9999
print s.score
