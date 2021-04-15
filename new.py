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
        print(self.a)
        print(self.c) #acess inside class

t=Test()
t.m1()
print(t.a,t.b) #ouside the class


t.d=40 #adding instance variables outside of a class
print(t.__dict__)


#  how to delete member variables of class 
# syntax - del self.variablename -inside clas
#syntax- del objectrefrence.variablename -outsideclass

class Test1:

    def __init__(self):
        self.x=10
        self.y=20
        self.z=30

    def m(self):
        del self.z
t1=Test1()
print(t1.__dict__)
t1.m()  #execting inside
print(t1.__dict__)

del t1.x  #executing outside

print(t1.__dict__)

# using objects

t2=Test1()  

t3=Test1()

del t3.z

print(t2.__dict__)
print(t3.__dict__)


