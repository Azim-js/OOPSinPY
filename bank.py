import sys

class Customer:
    bankname="Azim's BANK"

    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposit(self,amt):
        self.balance=self.balance+amt
        print("AFTER THE DEPOSIT THE BALANCE AMOUNT IS : RS ",self.balance)
        print("---------------------------------------------------------------------------------------- \n")

    def withdraw(self,amt):
        if amt>self.balance:
            print("INSIFUCIENT FUNDS IN BALANCE PLEASE DEPOSITE !")
            print("----------------------------------------------------------------------------------- \n")
            sys.exit()
        self.balance=self.balance-amt
        print("AFTER THE WITHDRAW THE BALANCE AMOUNT IS : RS ",self.balance) 
        print("--------------------------------------------------------------------------------------- \n")   


print("------------------------------------------- WELCOME TO ",Customer.bankname,"---------------------------------------------")    

name=input("ENTER YOUR NAME : ")
c=Customer(name)

while True:
    option=input(" CHOOSE AN OPTION \n d-> Deposit \n w-> Withdraw \n e->Exit \n")

    if option=='d' or option=='D':
        amount=float(input("ENTER THE AMOUNT TO DEPOSIT : "))
        c.deposit(amount)

    elif option=='w' or option =='W':
        amount=float(input("ENTER THE AMOUNT TO WITHDRAW : "))
        c.withdraw(amount)

    elif option=='e' or option=='E':
        print(" THANK YOU FOR USING OUR SERVICES")        
        sys.exit()
    else:
        print('INVALID OPTION ... PLEASE CHOOSE A CORRECT OPTION')    