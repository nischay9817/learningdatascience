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

# class Account:
#     def __init__(self,accountno,balance):
#         self.accountNo = accountno
#         self.balance = balance
    
#     def debit(self,deductAmount):
#         self.balance = self.balance - deductAmount  
    
#     def credit(self, inputAmount):
#         self.balance = self.balance + inputAmount
    
#     def checkingBalance(self):
#         print(f"Checking current balance {self.balance}")

# A1 = Account(17874594656,200000)
# A1.checkingBalance()
# A1.credit(100000)
# A1.checkingBalance()
# A1.debit(100000)
# A1.checkingBalance()

# deleting the object
# class Student:
#     def __init__(self,name):
#         self.name = name

# s1 = Student("Nischay")
# # print(s1)

# del s1
# print(s1)

# private concept of oop
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

# acc1 = Account("12345","20000")
# print(acc1.acc_no)
# print(acc1.__acc_pass)


# inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("Car started...")
    
#     @staticmethod
#     def stop():
#         print("Car stopped...")

# # inherited:
# class Toyota(Car):
#     def __init__(self,name):
#         self.name = name

# car1 = Toyota("book")

# print(car1.start())

# super() method
# class Car:
#     def __init__(self,type):
#         self.type = type

# class Toyota(Car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)

# car1 = Toyota("Fornutnur", "Petrol")
# print(car1.type)


# class Person:
#     name = "Anonymous"
#     def changeName(self,name):
#         Person.name = name


# p1 = Person()

# p1.changeName("Nischay")

# print(p1.name)
# print(Person.name)



# class method 
# class Student:
#     name = "anonymous"
#     @classmethod
#     def changeName(cls,name):
#         cls.name = name

# s1 = Student()
# s1.changeName("Nischay")
# print(s1.name)
# print(Student.name)

# @Property method in python
# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
    
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math)/3) + "%"

# stu1 = Student(98,97,99)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.phy)
# print(stu1.percentage)


# print([1, 2, 3]+[4, 5, 6])

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real,"i+",self.img,"j")
    
    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(1,5)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1.add(num2)
num3.showNumber()