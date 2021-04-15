class Employee:
    
    def __init__(self):
        self.eno=1
        self.ename='Azim'
        self.eage=21
        self.esal="NIL"


e=Employee()


print(e.__dict__)    

class Student:
    ''' this is student class '''
    def __init__(self,x,y,z):
        self.name=x
        self.age=y
        self.rollno=z

    def display(self):
        print("Student Name: {} \n Student Age : {} \n Student rollno: {}".format(self.name,self.age,self.rollno))

print(Student.__doc__)
s1=Student('Azim',21,'1pse17cs55')
s2=Student('Hari',21,'1pse17cs89')

s1.display()
s2.display()

# INSIDE INSTANCE METHOD by using self Variable

class Test:

    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        self.c=30

t=Test()
t.m1()
print(t.__dict__)
