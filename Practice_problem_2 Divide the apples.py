print("We are going to divide the apples to all the students")
no_of_apples = int(input("Enter the total number of Apples given by your friends : "))
minimum = int(input("Minimum number of students :"))
maximum = int(input("Maximum number of students : "))
print("\n")
for i in range(minimum, maximum + 1):
    if no_of_apples % i == 0:
        print(f"{no_of_apples} Apples can be equally distributed in {i} Students. \n")
    elif no_of_apples % i != 0:
        print(
            f"{no_of_apples} Apples cannot be equally distributed in {i} Students. \n {no_of_apples % i} "
            f"Apples are extra or {i - (no_of_apples % i)} Apple is less . So we can't distribute it equally among all the students. \n")
    else:
        print("You Entered something Wrong...")