class  Human (object):
    __slots__=('__arm')
    def __init__(self,arm):
        self.__arm=arm
class Student(Human):
    __slots__=('__name','__score')
    def __init__(self,arm,name,score):
        super(Human,self).__init__(arm)
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score    
xiaoming = Student('xiaoming',99)
print(xiaoming.name)