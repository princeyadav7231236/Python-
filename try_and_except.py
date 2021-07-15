num1 = input("Enter First number : ")
num2 = input("Enter Second number : ")

try:
    print("The sum of two number is : ", int(num1) + int(num2))
except Exception as e :
    print(e)

print("This line is very important")