# List are ordinarily written as :
list_1 = []
for i in range(100):
    if i % 5 == 0:
        list_1.append(i)

print(list_1)  # Output --> [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# One liner format comprehension are written as :
list_2 = [i for i in range(50) if
          i % 2 == 0]  # Output --> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
print(list_2)

# ------------------------------------------------------------------------------
# Dictionary are ordinary written as :
dict_1 = {
    0: "item0",
    1: "item1",
    2: "item2",
    3: "item3",
    4: "item4",
    5: "item5"
}
print(dict_1)  # Output --> {0: 'item0', 1: 'item1', 2: 'item2', 3: 'item3', 4: 'item4', 5: 'item5'}

# One liner comprehensions are written as :

dict_2 = {i: f"item{i}" for i in range(6)}
print(dict_2)  # Output --> {0: 'item0', 1: 'item1', 2: 'item2', 3: 'item3', 4: 'item4', 5: 'item5'}


# -------------------------------------------------------------------------------
# Generators are ordinary written as :
def generator_1(n):
    for a in range(n):
        yield a


object_1 = generator_1(6)
print(object_1.__next__())  # Output --> 0
print(object_1.__next__())  # Output --> 1
print(object_1.__next__())  # Output --> 2
print(object_1.__next__())  # Output --> 3
print(object_1.__next__())  # Output --> 4
print(object_1.__next__())  # Output --> 5

print(list(object_1))  # This will print an empty list( [] ) because all the items are already printed.
print(list(object_1))   # Output --> [0, 1, 2, 3, 4, 5]  , The list will be printed when all the above command of the generator are commented

dresses = [dress for dress in ["dress1", "dress2", "dress1", "dress2"]]
print(type(dresses))  # Output --> List
print(dresses)

evens = (i for i in range(100) if i % 10 == 0)
print(type(evens))  # Output --> <class 'generator'>
print(evens)   # Output --> <generator object <genexpr> at 0x000001C4C9043CF0>
print(evens.__next__())
for i in evens:
    print(i)
print(list(evens))  # Output --> [10, 20, 30, 40, 50, 60, 70, 80, 90]
