# list1 = [["Diwakar", 1], ["Khushi", 1], ["Devil", 666], ["Happy", 1245]]
# dict1 = dict(list1)
# print(dict1)
# for item in dict1:
#     print(item)
#
# for item, value in dict1.items():
#     print(item, value)


lst2 = ["Diwakar", "Devil", "Khushi", 54, 56, 6, 22, 1, 3, 5]
for a in lst2:
    if str(a).isnumeric() and a > 6:
        print(a)


