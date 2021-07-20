def factorial(n):
    a, b = 1, 2
    for i in range(n):
        yield a
        a, b = b, b+1

def fac(num):
    if num < 2:
        return 1
    return num*fac(num-1)

def res_fac(number):
    print(f"The number to be multiplied to get the factorial are :-  {list(factorial(number))}")
    print(f"The Factorial of {number} is {fac(number)} ")

num1 = factorial(5)
print(list(num1))  # This will print the list of the numbers of the numbers to which we will multiply and get the answer of factorial of the given number

print(fac(5))

res_fac(5)