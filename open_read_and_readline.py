a = open("sample.txt", "rt")
print(a.read())
# print(a.readline())
# print(a.readline())
# print(a.readlines())

# content = a.read()
# for line in a:
#     print(line, end=" ")
# print(content)

content = a.read(5456456)
# print("1.)       ", content)
# print("2.)       ", content)
print(a.tell())

a.close()