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