# import types

# class Student(object):
#     def __init__(self,name,score):
#         self.__name=name
#         self.score=score
#     def print_name(self):
#         print(self.__name)
#     def set_name(self,name):
#         self.__name=name
#
#     pass
# bart=Student('kevin',18)
# bart.set_name('kev')
# bart.print_name()
#
# def fn():
#     pass
# print(type(fn)==types.FunctionType)
# print(type('anc')==str)
# print(type(abs)==types.BuiltinFunctionType)
# print(type(lambda x:x)==types.LambdaType)
# print(type(( x for x in [1,3]))==types.GeneratorType)
# print(type(int)==types.TypeType)


from types import MethodType
#创建一个方法
def set_age(self, arg):
    self.age = arg
#创建一个类
class Student(object):
    pass
s_one=Student()
Student.set_age=MethodType(set_age,Student)
s_one.set_age(12)
print(s_one.age)


class Test(object):
    def __init__(self):
        self.__money=40
    def getMoney(self):
        return self.__money
    def setMoney(self,val):
        self.__money=val
    money=property(getMoney,setMoney)
test= Test()
print(test.money)      
test.money=1000
print(test.money)  



class Human(object):
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,val):
        print('-----------')
        self.__height=val
        print(self.__height)
human=Human()
human.height =999
  

