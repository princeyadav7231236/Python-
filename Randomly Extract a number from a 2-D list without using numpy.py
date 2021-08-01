import random
mylist = [
[0, 1, 2, 3, 4, 5],
[0, 1, 2, 3, 4, 5],
[0, 1, 2, 3, 4, 5],
[0, 1, 2, 3, 4, 5],
[0, 1, 2, 3, 4, 5],
[0, 1, 2, 3, 4, 5]]

def random_num():
    i = -1
    while True:
        if i == len(mylist[i])-1:
            break
        for item in mylist[i]:
            i += 1
            random_number = random.choice(mylist[i])
            mylist[i][random_number] = "x"

random_num()
for item in mylist:
    print(item)

# Output -->
# ['x', 1, 2, 3, 4, 5]
# [0, 1, 2, 'x', 4, 5]
# [0, 1, 2, 'x', 4, 5]
# [0, 1, 2, 3, 'x', 5]
# [0, 1, 2, 3, 'x', 5]
# [0, 1, 2, 3, 'x', 5]
