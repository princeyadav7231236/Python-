# num1 = int(input("Enter the size of the triangle which you want to make : "))
# var1 = input("Enter the symbol of which you want to print the triangle : ")
# for i in range(1, num1+1):
#     print(i*var1)

# num1 = int(input("Enter the size of the triangle which you want to make : "))
# var1 = input("Enter the symbol of which you want to print the triangle : ")
# for i in range(1, num1+1):
#
#     print(((num1+1)-i)*var1)

def func1(a, q):
    for i in range(1, q+1):
        b = i + (a - 1)
        print(i * str(b))
        q -= 1
        if q == 0:
            break


u = int(input("Enter the number from where you want to start : "))
o = int(input("Enter the size of the triangle : "))
func1(u, o)
