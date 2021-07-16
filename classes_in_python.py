class Student:
    pass


Harry = Student()
Diwakar = Student()
Harry.name = "Harry"
Diwakar.name = "Diwakar"
Harry.std = 10
Diwakar.std = 12
Diwakar.subjects = ["Maths", "Physics", "Chemistry", "IP"]
print(Diwakar.name, Diwakar.std, Diwakar.subjects)  # output = Diwakar 12 ['Maths', 'Physics', 'Chemistry', 'IP']
print(Harry.name)  # output = Harry
print(Harry.std)  # output = 10
