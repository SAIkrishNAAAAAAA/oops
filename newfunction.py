



#In this challenge, you need to implement a method that squares passing variables and returns their sum.

# Sample method output 35

# Coding exercise Create a class Point with three properties: x, y, and z.

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sqSum(self):
        result = ((self.x**2) + (self.y**2 )+ (self.z**2))
        return result          
num1 = int(input("enter a numbers:"))
num2 = int(input("enter a numbers:"))
num3 =int(input("enter a numbers:"))
sum = Point(num1,num2,num3)
print( sum.sqSum())

# Challenge 2: Implement a Calculator Class

class Calculator:

    def __init__(self,x,y):
        self.x =x
        self.y =y
    def add(self):
        return self.x+self.y
    def subtract(self):
        return self.x-self.y
    def multiply(self):
        return self.x*self.y
    def divide(self):
        return self.x/self.y
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
obj = Calculator(num1,num2)
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())

# Challenge 3: Implement the Complete Student Class

class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

obj =Student ()

obj.setName("saikrishna") 
obj.setRollNumber(143)
print(obj.getName())
print(obj.getRollNumber())

# Challenge 4: Implement a Banking Account

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

account = Account("Ashish", 5000)
print(account.title)    
print(account.balance)  


savingsAccount = SavingsAccount("Ashish", 5000, 5)
print(savingsAccount.title)        
print(savingsAccount.balance)   
print(savingsAccount.interestRate)

# Challenge 5: Handling a Bank Account

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.balance * self.interestRate) / 100

demo1 = SavingsAccount("Ashish", 2000, 5)  
demo1.deposit(500)                         
print(demo1.getBalance())                   

demo1.withdrawal(500)                       
print(demo1.getBalance())                   

interest = demo1.interestAmount()           
print(interest)                             
