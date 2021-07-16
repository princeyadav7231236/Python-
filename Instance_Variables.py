class Employee:
    """This is a Employee class"""   # This is a __doc__ string, this is very helpful when creating a larger program.
    no_of_leaves = 5
    pass


Harry = Employee()
Diwakar = Employee()
Harry.name = "Harry"
Harry.salary = 5000000
Harry.role = "Instructor"

Diwakar.name = "Diwakar"
Diwakar.salary = 1000000000
Diwakar.role = "Developer"

print(Employee.no_of_leaves)
print(Employee.__dict__)    # This will print the Dictionary of objects in the Employee class.
Employee.no_of_leaves = 7
print(Employee.__dict__)    # This will print the Dictionary of objects in the Employee class.
print(Employee.no_of_leaves)
