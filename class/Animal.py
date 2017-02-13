# -*- coding:utf-8 -*-
#继承
class Animal(object):
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
