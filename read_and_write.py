a = open("sample.txt", "w")
# print(a.read())   # This will give an error as in the given mode we cannot read anything as it is write mode
b = a.write("Hello Cutie. \n ")
# print(b)    # This will not print anything because the given mode is only write mode we cannot read anything in it .
a.close()

f = open("sample.txt", "a")
d = f.write("Yoo..... Khushi. \n")
# print(d)    # This will not print anything because the given mode is only write mode we cannot read anything in it .
f.close()

i = open("sample.txt", "r+")  # In this mode we can read and write both because this is r+ mode
print(i.read())
m = i.write("I think I like you Khushi. \n")
g = i.read()
print(g)
print(i.tell())
i.seek(12, 0)
print(i.read())
# print(m)                               # In this mode we cannot read the text which we have written in this mode
                                               # and if we try to print out the text it will give the output of number of words given in the text .
i.close()
