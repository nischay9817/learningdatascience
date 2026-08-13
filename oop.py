# creating the class
# class Student:
#     name = "Nischay"

# creating the object
# s1 = Student()
# print(s1)

# class Car:
#     color = "Blue"
#     brand = "BMW"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

# class Students:
#     def __init__(self,fullName):
#         self.name = fullName
#         print("Adding the new student in database...")

# s1 = Students("Nischay")
# print(s1.name)

# s2 = Students("Ram")
# print(s2.name)


# class Student:
#     college_name = "Central campus of technology"
#     def __init__(self,name):
#         self.name = name

# s1 = Student("Nischay")
# print(Student.college_name)
# print(s1.name)

# class Student:
#     college_name = "Central campus of technology"
#     name = "anonymous"
#     def __init__(self,name):
#         self.name = name

# s1=Student("Nischay")
# print(s1.name)

# creating the properties inside the class and calling it
# class Student:
#     def __init__(self,name):
#         self.name = name
    
#     def hello(self):
#         print("hello",self.name)

# s1=Student("Nischay")
# s1.hello()


# create a student class that takes name and marks of 3 subjects as arguments n constructor.then create a method to print average
# class Student:
#     def __init__(self, name, sub1, sub2, sub3):
#         self.name = name
#         self.math = sub1
#         self.science = sub2
#         self.english = sub3
    
#     def average(self):
#         average = (self.math + self.science + self.english)/3
#         print(average)

# s1 = Student("Nischay",100,100,50)
# s1.average()


# another method 
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Your average score is",sum/3)

# s1 = Student("Nischay",[99,97,96])
# s1.avg()


# static method:
# class Student:
#     @staticmethod
#     def college():
#         print("ABC college")
        
# s1 = Student()
# s1.college()


# abstraction
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
    
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car started...")

# car1 = Car()
# car1.start()


# create account class with 2 attributes balance and account number. Create methods for debit, credit and printing the balance

class Account:
    def __init__(self,accountno,balance):
        self.accountNo = accountno
        self.balance = balance
    
    def debit(self,deductAmount):
        self.balance = self.balance - deductAmount  
    
    def credit(self, inputAmount):
        self.balance = self.balance + inputAmount
    
    def checkingBalance(self):
        print(f"Checking current balance {self.balance}")

A1 = Account(17874594656,200000)
A1.checkingBalance()
A1.credit(100000)
A1.checkingBalance()
A1.debit(100000)
A1.checkingBalance()