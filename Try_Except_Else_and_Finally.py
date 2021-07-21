def divide(a, b):
    try:
        print(f"{a} / {b} is {a / b}")
    except Exception as e:
        print(e)
    else:
        print("No Exception")


divide(1, 2)  # Output --> 1 / 2 is 0.5
#  No Exception

# ------------------------------------------------------------------------------

f1 = open("sample.txt")
try:
    f = open("Does2.txt")
except EOFError as e:
    print("EOF error ---> ", e)
except IOError as e:
    print("IO error ---> ", e)    # Output --> IO error --->  [Errno 2] No such file or directory: 'Does2.txt'
except Exception as e:
    print(e)
else:
    print("No Exception ")
finally:
    f1.close()
    # f.close()