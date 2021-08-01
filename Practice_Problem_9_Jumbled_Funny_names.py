import random

item = []
list_of_first_names = []
list_of_last_names = []
jumbled_list = []


def jumbled_names(asize, *args):
    i = 0
    for items in args:
        words = items.strip().split()
        item.append(words)
    print(item)
    for a in item:
        list_of_first_names.append(item[i][0])
        list_of_last_names.append(item[i][1])
        i += 1
        if i == len(item):
            break
    print(list_of_first_names)
    print(list_of_last_names)

    for i in range(asize):
        new_list = list_of_first_names[i] + list_of_last_names[random.randint(0, asize)]
        jumbled_list.append(new_list)
    print(jumbled_list)


if __name__ == '__main__':
    list_of_friends = ["Rohan Das", "Ritesh Arora", "Shubham Agarwal"]
    size = 2
    jumbled_names(size, *list_of_friends)
