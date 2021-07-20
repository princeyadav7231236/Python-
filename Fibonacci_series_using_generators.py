# Fibonacci series --> 1  1   2   3   5   8   13   21   34   55   ..........

def fibonacci_series(number):
    a, b = 0, 1
    for i in range(number):
        yield a
        a, b = b, a+b

    """
    if n = 5
    n(4) + n(3)
    n(3) +n(2) + n(2) + n(1)
    n(2) + n(1) + n(0) + n(1) + n(0) + n(1) + n(1)
    n(0) + n(1) + n(1) + n(0) + n(1) + n(0) + n(1) + n(1)
    1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 8
    """

num1 = fibonacci_series(6)
print(num1.__next__())
print(num1.__next__())
print(list(num1))

for i in num1:
    print(i)
