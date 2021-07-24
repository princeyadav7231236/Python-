# a = input("What is your name : ")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed ! ")
#
# b = input("How much you earn : ")
# if int(b) == 0:
#     raise ZeroDivisionError

c = input("Enter your name : ")
try:
    print(a) # It will give an error
except Exception as e:
    if c == "Devil":
        raise ValueError("Devil is blocked because he is the Devil. ")

print("Exception Handled ")
