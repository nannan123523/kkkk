# -*-coding:UTF-8 -*-

class Person:
    #定义一个类 类里面有属性和方法
    def __init__(self, name, age):
        # 传入三个形参，self可以里面为谁调用就是谁，比如下面的p和h，就是调用self
        self.name = name
        self.age = age
    def desc(self):
        print("我叫%s，今年%d岁" % (self.name, self.age))
p=Person('nihao',25)
#类的调用
p.desc()
#类的方法调用
h=Person('shabi',55)
h.desc()