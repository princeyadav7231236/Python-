list1 = input("Enter the list \n")
splitting = list1.split(" ")
list_2 = list(splitting)


def first_method():
    list_2.reverse()
    return list_2
    # print(list_2)


def second_method():
    print(list_2[::-1])


def third_method():
    mn = 0
    mx = len(list_2)

    while mx >= -1:
        mn += 1
        mx -= 1
        for i in range(mn, mx):
            list_2[mn - 1], list_2[mx] = list_2[mx], list_2[mn - 1]
    print(list_2)

if __name__ == '__main__':
    print(first_method())
