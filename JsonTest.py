import json
d = dict(name='Mark',age=24,score=100)
str = json.dumps(d)
print str
ob = json.loads(str)
print ob

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score= score

def student2dict(std):
        return {
            'name':std.name,
            'age':std.age,
            'score':std.score
        }
s = Student('Mark',23,100)
print(json.dumps(s,default=student2dict))
