class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print("%s:%s"%(self.__name,self.__score))
    def get_grade(self):
        if self.__score > 100 :
            print('you grade is A , you are facking excenlent')
        else:
            print('you suck') 
    def get_score(self):
        return self.__score    
    def set_score(self,score):
        if(0 <= score <=100):
            self.__score = score         

xiaoming = Student('xiaoming',888) 
xiaoming.print_score()     
xiaoming.get_grade()  
print(xiaoming._Student__name)
print(isinstance(xiaoming,Student))
print(isinstance(True,bool))
print(dir(xiaoming))
setattr(xiaoming,'x',999)
print(getattr(xiaoming,'x'))
print(hasattr(xiaoming,'x'))
 