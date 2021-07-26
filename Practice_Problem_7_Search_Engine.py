list_of_words = ["Python is a good programming language", "Python is a programming language it is not the Python Snake",
                 "C++ and c# is the best fastest programming language", "Java is used in Web Development."]
user_input = input("Enter the word here you want to search : ")

list_1 = []
for i in range(len(list_of_words)):
    b = list_of_words[i].lower().count(user_input.lower())
    list_1.append(b)  # Appending the values of the user_input in the list
list_2 = list_1[:]  # Creating a copy of list 1
list_2.sort()
list_2.reverse()
# print(list_2)
# [1, 2, 0]
# [2, 1, 0]

i = -1
print(f"Showing results of {user_input} ! \n ")
while True:
    i += 1
    if user_input.lower() in list_of_words[list_1.index(list_2[i])].lower():  # This will check whether the user input is in the list or not
        print(f"{i +1}.  {list_of_words[list_1.index(list_2[i])]}")
    if i == len(list_of_words) - 1:
        break
