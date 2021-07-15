lst1 = [1, 2, 3, 4, 5, 6]
a = list(map(str, lst1))
# print(a)

# for i in range(len(lst1)):
#     lst1[i] = str(lst1[i])

lst1[2] = lst1[2] + 1


# print(lst1[2])


def sq(p):
    return p * p


res = sq(5)


# print(res)

# num1 = list(map(sq, lst1))
# print(num1)


def cube(num6):
    return num6 * num6 * num6


#
# func = [num1, cube]
# for i in range(5):
#     val = list(map(lambda x: x * i, lst1))
#     print(val)
#

# def is_greater(num):
#     return num > 5
#
#
# gr_than_5 = list(filter(is_greater, lst1))
# print(gr_than_5)
#


from functools import reduce
num = reduce(lambda x, y: x*y, lst1)
print(num)

