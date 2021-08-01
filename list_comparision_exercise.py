# The problem is that we have to take all the even numbers of the given list and put it in a new list
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  # Given list
even = []  # New empty list,  we will keep all the even numbers of the list .
odd = []  # New empty list,  we will keep all the odd numbers of the list .
for item in a:
    if item % 2 == 0:
        even.append(item)
    elif item % 2 != 0:
        odd.append(item)

print(even)   # Output --> [4, 16, 36, 64, 100]
print(odd)    # Output --> [1, 9, 25, 49, 81]
