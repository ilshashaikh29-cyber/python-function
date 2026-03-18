#What is a function?
#A function is a block of code that runs only when it is called.

#why use functions?

#1.Avoid repeating code
#2.Makes program clean and organized
#3.Easy to debug and reuse

#syntax:
#def function_name():
    #code

#ex:
#def greet():
# print("Hello students")

# greet()

# Function with Parameters
# Used to pass values

# def greet (name):
#       print (f"Hello {name}")

# greet()
# greet("shreyarth")
# greet("AICW")

#Task 2 
# Create a function to creat if a number is even or odd
# num=int(input("enter a num"))
# def check_even_odd(num):
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# # check_even_odd(4)
# # check_even_odd(7)
# result=check_even_odd(num)
# print(result)

#Task 3
# Create a function to find the factorial of a number 
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)
# num=int(input("enter a number:"))
# print("factorial:",factorial(num))

#Task 4
#create a function to find maximum of three numbers
# def maximum(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c

# # User input
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# z = int(input("Enter third number: "))

# print("Maximum number is:", maximum(x, y, z))

#Task 5
#Create a function to check if a string is palindrome 
# def is_palindrome(s):
#     return s == s[::-1]

# Example
# text = input("Enter string: ")
# if is_palindrome(text):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#Task 6
#create a function to calculate area of circle.
# def area_of_circle(radius):
#     return 3.14 * radius * radius

# # Example
# r = float(input("Enter radius: "))
# print("Area of circle:", area_of_circle(r))




