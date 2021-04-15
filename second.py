
# VArious places to declare static Variables
class Test:
    a=10
    def __init__(self):
        Test.b=20

    def m1(self):
        Test.c=30

    @classmethod
    def m2(cls):
        cls.d1=40
        Test.d2=400

    @staticmethod
    def m3():
        Test.e=50


print(Test.__dict__)

t=Test()

print(Test.__dict__)

t.m1()
print(Test.__dict__)

Test.m2()
print(Test.__dict__)

Test.m3()
print(Test.__dict__)

Test.f=60
print(Test.__dict__)


# acces Static VAriables

print(Test.a)
print(t.a)

# modify the value of static variable

class Test1:
    a=777
    @classmethod
    def m1(cls):
        cls.a=888

    @staticmethod
    def m2():
        Test1.a=999

print(Test1.a)
Test1.m1()
print(Test1.a)

Test1.m2()
print(Test1.a)