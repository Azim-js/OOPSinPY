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