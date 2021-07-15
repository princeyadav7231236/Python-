# a = lambda num1, num2, num3: print(f"The sum of {num1} ,  {num2} and  {num3} is {num1 + num2 + num3}")
# # print(f"The sum is ", a(33, 34, 33))
# b = (a(33, 33, 34))
# print(b)
#
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = (list(map(lambda x: x ** 3, list1)))
# print(result)

a = [1, 2, 3, 45, 65, 100, 4555]
b = [45, 100, 12, 78]
res = list(filter(lambda x: x in a, b))
print(res)
c = [2, 3, 5]

from functools import reduce

var1 = reduce(lambda x, y: x * y, c)
print(var1)
