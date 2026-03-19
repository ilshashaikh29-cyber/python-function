# What is OOP?
# OOP is a way of writing code  using objects and classes.

# Key feature of OOPs
# 1.class :  Blueprint (design)

# #Ex:
# class Student:
#     pass

# 2.object :Instance of a class
    
#     s1=Student()
#     "Class= design,object=real thing"

# 3.Constructor (___init__)
# Automatically runs when object is  created

# Class Student:
#     def__init_-(self,name):
#     self.name=Name

# s1=Srudent("ilsha")

# 4. self Keyword
# Refers to currennt object

# class Student:
#     def __init__(self,name):
#         self.name=name

# s1=Student("Ilsha")
# print(s1.name)
# output:Ilsha

# self.name stores value inside object

# 5.Methods (function inside class)
# class Student:
#     def greet(self):
#         print("hello")
# s1=Student()
# s1.greet()


#output:hello

# #full example
# class Student:
#     def __init__(self,name):    #constructor with parameter
#         self.name=name          #self.name is instance variable
#     def greet(self):             #method to greet ,self>access instance
#         print(f"hello{self.name}")     #print the stmt
# s1=Student("ilsha")         #creating the object
# s1.greet()                  #calling the method to greet 
# #output:Hello ilsha

# class car:
#     def __init__(self,brand):
#         self.name=brand
#     def greet(self):
#         print(f"Driving {self.name}")
# s1=car("BMW")
# s1.greet()
        
# class car:
#     def __init__(self,brand,name,model):
#         self.brand=brand
#         self.name=name
#         self.model=model
#     def drive(self):
#             print("f{self.name}is  driving {self.brand} {self.model}")
# car1=car("BMW","Ilsha","2025")
# car1.drive()

# class employee:
#     def __init__(self,firstname,lastname,age,role,salary):
#         self.firstname=firstname
#         self.lastname=lastname
#         self.age=age
#         self.role=role
#         self.salary=salary

#     def work(self):
#         print(f"{self.firstname} {self.lastname} the age is {self.age} is working as {self.role} and the salary is  {self.salary}")


# em=employee("ilsha","shaikh","20","CEO","5,00,000")
# em.work()