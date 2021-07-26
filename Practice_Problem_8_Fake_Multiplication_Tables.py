import random

rohanList = []
mylist = []

def rohanMultiplication(n):
    a = random.randint(1, 10)
    b = random.randint(1, n-1)

    for i in range(1, 11):
        rohanList.append(n * i)

    rohanList[a] = (n * a) + b
    return rohanList

def isCorrect(number):
    while True:
        for i in range(1, 11):
            mylist.append(number * i)
        return mylist

if __name__ == '__main__':
    table_of_number = int(input("Enter the number of which you want to know the table : \n"))
    rohan_function = rohanMultiplication(table_of_number)
    my_function = isCorrect(table_of_number)
    x = -1
    print(f"Rohan's list --->  {rohanList}")
    print(f"My list --->  {mylist}")
    while True:
        x += 1
        if x == 10:
            break
        if rohanList[x] == mylist[x]:
            pass
        elif rohanList[x] != mylist[x]:
            print(f"The value of Rohan's list is wrong at position {x +1} the value Rohan's list has printed {rohanList[x]} but the correct  value is {mylist[x]}")

    print("This all shows that Rohan is a fraud and he was doing fraud with all of us.")
