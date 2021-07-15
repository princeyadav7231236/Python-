a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))


def func1(c, d):
    print("The sum of two number is : ", a + b)


# func1(a, b)
# w = func1(a, b)
# print(w)

def func2(c, d):
    """This is a function to calculate the average of two number """
    p = (c + d) / 2
    # print(p)
    return p


i = func2(a, b)
print(func2.__doc__)      # This is a docstring
print(i)
