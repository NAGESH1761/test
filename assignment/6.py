# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
#Implement BankAccount class with at least three methods
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
  
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
  
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
  
    def display(self):
        print("\n Net Available Balance=",self.balance)
  

# creating an object of class
N = Bank_Account()
   
# Calling functions with that class object
N.deposit()
N.withdraw()
N.display()
##Output:
##
##Hello !!! Welcome to Deposit&Withdrawal Machine
##Enter amount to be deposited: 
## Amount Deposited: 1000.0
##Enter amount to be withdrawn: 
## You Withdrew: 500.0

## Net Available Balance = 500.0
