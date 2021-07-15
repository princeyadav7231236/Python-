with open("sample.txt") as f, open("sample2.txt") as i:       # To open multiple file simultaneously we use with function while using with function we
                                                                                              # need not to close the file which are opened get automatically closed
    u = f.readlines()
    print(u)
    o = i.readlines()
    print(o)
    # f.close()    # While using with function we need not to close the with block of code the file which are opened get automatically closed
    # i.close()

