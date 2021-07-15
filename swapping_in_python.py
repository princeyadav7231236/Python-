# Traditional Method
a = 45
b = 55
temp = a
a = b
b = temp
print(a, "\n", b)

# Python's easy method
a, b = b,a
print(a,"\n",b)