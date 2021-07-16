class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Diwakar", 17)
print(p1.name)  # Output = Diwakar
print(p1.age)  # Output = 17


# -------------------------------------------------------

class Employee:
    no_of_leaves = 5

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"The name is {self.name}. The salary is {self.salary}. The role is {self.role}."


Diwakar = Employee("Diwakar", 1000000000, " Game Developer")
print(Employee.print_details(Diwakar))  # Output --> The name is Diwakar. The salary is 1000000000. The role is  Game Developer.
print(Diwakar.salary)  # Output ---> 1000000000

