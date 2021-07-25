print("Enter the number of items you want to enter , (Enter one by one) : \n")
size = int(input("Enter the size : \n"))

# Creating an empty list in which we will append the values of which we want to know the Palindrome.
my_list = []
for i in range(size):
    my_list.append(input("Enter the element one by one : "))  # This will take the input of the items/elements

print(f"Your Elements are {my_list}")  # This will print the list

# my_list = ["45", "24", "15", "42"]    # This is the sample list

for item in my_list:
    if item == str(item)[::-1]:   # If the item is equal to the Palindrome of the item then it will print the same output
        print(f"Palindrome of {item} is {str(item)[::-1]}")
    elif item != str(item)[::-1]:  # If the item is not equal to the Palindrome of the item then it will add 1 to the value
                                              # and it will keep it adding up to when the item value is not equal to its Palindrome
        a = int(item)
        for i in range(10000000):
            b = a + i
            if str(b) == str(b)[::-1]:
                print(f"The Palindrome {item} is {str(b)[::-1]}")  # This will print the Next Palindrome after the item which was not having the Palindrome.
                break
