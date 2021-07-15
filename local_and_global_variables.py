l = 45


def func1(a, b):
    # l = 12
    m = 55
    print("The value of l is : ", l)
    print("The value of m is : ", m)


func1(445, 55)

a = 45


def func2():
    # a = 20

    def func3():
        global a
        a = 55

    print("Before calling func3 the value of a is ", a)
    func3()
    print("After calling func3 the value of a is ", a)


func2()
print(a)
