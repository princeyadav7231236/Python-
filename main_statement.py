# import enumerate_functions
#
# print(enumerate_functions.__name__)
# print(__name__)


def print_string(string):
    return f"Ye karke dikhao..... {string}"


def add(n1, n2):
    return f"The sum of {n1} and {n2} is  {n1 + n2} "


print(f"and the name is {__name__}")
if __name__ == "__main__":
    print(print_string("are ye.....ye.....ye karke dikhao"))
    a = add(55, 45)
    print(a)
