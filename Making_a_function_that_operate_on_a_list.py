list1 = ["1", "2", "3"]

def operations_on_a_list():

    size = int(input("Enter the number of elements you want to add in the list : "))

    for i in range(size):

        value = input("Enter the element you want to add in the list : ")

        list1.append(value)

    return list1

print(operations_on_a_list())





