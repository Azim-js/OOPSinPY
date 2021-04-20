class Student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return name 

    def setMarks(self,marks):
        self.marks=marks

    def getMarks(self):
        return marks


n=int(input("ENter number of students: "))

for i in range(n):
    print("----------------------------------------------------------------")
    s=Student()
    name=input("ENter The student NAme: ")
    s.setName(name)
    marks=int(input("enter the Student Marks: "))
    s.setMarks(marks)


    print("HI: ",s.getName())
    print("YOUR MARKS ARE : ",s.getMarks())
    print()