class Employee:
    no_of_leaves = 5

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    def __add__(self, other):
        return f"The Addition of two persons salary is {self.salary + other.salary}"

    def __truediv__(self, other):
        return f"The True Division of two persons salary is {self.salary / other.salary}"

    def __repr__(self):
        return f"Employee {self.name}, Salary is {self.salary}, and role is {self.role}."

    def __str__(self):
        return f"The name is {self.name}, Salary is {self.salary}, and role is {self.role}."

emp1 = Employee("Devil", 1000000000, "VR Game Developer")
emp2 = Employee("Devil", 1000, "VR Game Developer")
print(str(emp1))
print(emp1.__add__(emp2))
print(emp1.__truediv__(emp2))
print(emp1.__repr__())
