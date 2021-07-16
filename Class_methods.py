class Employee:
    no_of_leaves = 5

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"The name is {self.name}. The salary is {self.salary}. The role is {self.role}."

    @classmethod
    def Change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves


Diwakar = Employee("Diwakar", 1000000000, " Game Developer")
Harry = Employee("Harry", 1000000, " Programmer ")
print(Diwakar.no_of_leaves)  # Output --> 5
Harry.Change_leaves(7)  # We are changing the no_of_leaves of Harry but it changes it for whole class, i mean for every object the change has been made
                                        # so, when any object calls for no_of_leaves after doing the changes the changes will be implemented to all the objects

print(Diwakar.no_of_leaves)  # Now it will give the Output 7 because now the change has been implemented to all the objects.
                                               # This is the use class methods to implement changes to all objects at one go.
