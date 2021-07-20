class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email_1 = f"{self.first_name}.{self.last_name}@codewithdevil.com"

    def Explain(self):
        return f"The employee name is {self.first_name} {self.last_name}"

    @property
    def email(self):
        if self.first_name == "none" or self.last_name == "none":
            return "Email is not set. please set it using setter."
        return f"{self.first_name}.{self.last_name}@codewithdevil.com"

    @email.setter
    def email(self,string):
        print("Setting now ........")
        names = string.split("@")[0]
        self.first_name = names.split(".")[0]
        self.last_name = names.split(".")[1]

    @email.deleter
    def email(self):
        self.first_name = "none"
        self.last_name = "none"

hindustani_supporter = Employee("Hindustani", "Supporter")
print(hindustani_supporter.email)

hindustani_supporter.email = "U.S"
print(hindustani_supporter.email)

hindustani_supporter.email = "This.That"
print(hindustani_supporter.email)
print(hindustani_supporter.first_name)
print(hindustani_supporter.last_name)

del hindustani_supporter.email
print(hindustani_supporter.email)
hindustani_supporter.email = "Devil.Coder"
print(hindustani_supporter.email)