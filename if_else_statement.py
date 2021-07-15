# a = input("Enter First number : ")
# b = input("Enter Second number : ")
# if a > b:
#     print(a, " is greater then ", b)
# elif a == b:
#     print(a, "is equal to ", b)
# else:
#     print(a, " is less then ", b)

# lst1 = [1, 3, 45, 21, 77, 23, "Devil", "Khushi", "Diwakar"]
# print(24 in lst1)
# print("khushi " in lst1)
# print("Khushi " in lst1)   # This will give an error because a extra space is also given
# print("Khushi" in lst1)
#
# if "Devil" not in lst1:
#     print("No it is not in the list")
# else:
#     print("It is in the list")


# ..............Quiz..............
age = int(input("Enter your age :   "))
if age > 100:
    print("You can't get an Driving License because you are old or dead")
elif age == 18:
    print("We can't decide weather we should give you the driving license or not ")
elif age > 18:
    print("You can get the driving license ")
elif age < 1:
    print("You are not yet born")
else:
    print("You're a kid")
