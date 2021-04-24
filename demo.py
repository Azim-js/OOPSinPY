class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs ..'.format(name,cls.legs))

Animal.walk('Dog')        
Animal.walk('cat')

#  Program to track the number of objects created for a class

class Test:
    count=0 #this is class variable 
    def __init__(self):
        Test.count=Test.count+1

    @classmethod
    def noOfObject(cls):
        print("The number of objects CReated are for the class ",cls.count)


t1=Test()
t2=Test()

Test.noOfObject()

t3=Test()
t4=Test()
t5=Test()

Test.noOfObject()

# PASSING members of one class to another class

class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal

    def display(self):
        print('Employee Number :',self.eno)    
        print('Employee Name:',self.ename)
        print("EMployee Salary:",self.esal)

class Tests:
    def modify(emp):
        emp.esal=emp.esal+1000
        emp.display()

e=Employee(100,'Azim',10000) 
e.display()    
Tests.modify(e)
