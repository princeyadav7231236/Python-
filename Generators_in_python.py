def generator_of_a_number(number):
    for a in range(number):
        yield a

num1 = generator_of_a_number(12)
print(num1.__next__())  # This will produce the output for only one value
print(num1.__next__())
print(num1.__next__())
print(num1.__next__())

print(generator_of_a_number(12))  # This will print the generator of the value

for i in num1:
    print(i)

var1 = "455532"   # Iter is only not valid for integer type so it must be an string or other type like list, tuple, etc.
ier = iter(var1)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

for i in ier:
    print(i)
