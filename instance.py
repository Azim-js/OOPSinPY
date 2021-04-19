class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print('Hi',self.name)   
        print("Your Marks are :",self.marks)

    def grade(self):
        if self.marks>=60:
            print("You got First Grade")    

        elif self.marks>=50:
            print("You got Third Grade")        

        else:
            print("You Failed")    

n=int(input("Enter the number of Students: "))            

for i in range(n):
    print("------------------------------------------------------------------------------------")
    name=input("ENTER THE STUDENT NAME: ")
    marks=int(input("ENTER {}'s MARKS: ".format(name)))

    s=Student(name,marks)
    s.display()
    s.grade()
