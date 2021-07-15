# list1 = [" 1 ", " 2 ", " 3 ", "100"]
# a = " , "
# # print(a.join(list1))
# tup1 = ("Khushi", "Diwakar", "Serena")
# b = " and "
# # print(b.join(tup1))
#
# dict1 = {"Khushi": "Diwakar", "Diwakar": {"Khushi", "Serena"}, "Serena": "Diwakar"}
# # print(b.join(dict1))
#
# for key, value in dict1.items():
#     print(key, value)
#     if value == "Diwakar":
#         print(f"{key} is having crush on {value}")
#     if value == "Diwakar" and value > "2":
#         print(f"{key} thinks that {value} is a handsome boy")
#     else:
#         print("He is intelligent")

lis1 = ["Khushi", "Serena"]
# for item in lis1:
#     print(item, "and", end=" ")

c = " and ".join(lis1)
print(c, "....... I think I like them")