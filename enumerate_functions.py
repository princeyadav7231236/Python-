# list1 = ["Diwakar", "Khushi", 17, 16, "Devil"]
# # for index, val1 in enumerate(list1, 1):
# #     print(index, val1)
# a = 0
# for i in list1:
#     if a % 2 == 1:
#         print(i)
#     a += 1

# lst2 = ["Python ", "Programming ", "is ", "fun. "]
# for index, val in enumerate(lst2, 5):
#     print(index, val)

# lst2 = ["Python ", "Programming ", "is ", "fun. "]
# result = enumerate(lst2, 5)
# print(list(result))
#
l1 = ["Bhindi", "Aloo", "Chocolate", "Burger"]
# a = 1
# for item in l1:
#     if a % 2 != 0:
#         print(f"Serena please buy {item}")
#     a += 1

for index, value in enumerate(l1, 1):
    if index % 2 != 0:
        print(f"Serena please buy {value}")
