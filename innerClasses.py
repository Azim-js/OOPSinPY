class Outer:
    def __init__(self):
        print("outer class Object Creation")

    class Inner:
        def __init__(self):
            print("inner class onject creation")   

        def m1(self):
             print("inner class method")     

o=Outer()
i=o.Inner() #inner class object creation using outer creation
i.m1() #calling the inner class            

# Demo Program 

class Person:
    def __init__(self):
        self.name='Azim'
        self.db=self.Dob()

    def display(self):
        print("NAme: ",self.name)    

    class Dob:
        def __init__(self):
            self.dd=31
            self.mm=5
            self.yy=1999    

        def display(self):
            print('Dob={}/{}/{}'.format(self.dd,self.mm,self.yy))    

p=Person()
p.display()
x=p.db
x.display()       


