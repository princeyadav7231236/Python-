# def factorial(n):
#     """This  is the program to calculate the factorial of a given number """
#
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# num1 = int(input("Enter the number of which the factorial has to be calculated : "))
# print("The factorial of ", num1, " is ", factorial(num1))
#
#
# def fib(n):
#     """This  is the program to calculate the Fibonacci series at a given number"""
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#
#     return fib(n - 1) + fib(n - 2)
#
#
# num2 = int(input("Enter the number of which the fibonacci series has to be calculated : "))
# print("The Fibonacci series at ", num2, " is ", fib(num2))
#
def factorial_iterative(n):
    fac = 1
    for i in range(1, n+1):
        fac = fac * i
    return fac


num3 = int(input("Enter the number  : "))
print("The factorial of ", num3, " is ", factorial_iterative(num3))
