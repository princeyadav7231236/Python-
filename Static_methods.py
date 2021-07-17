class Employee:
    @staticmethod
    def print_good(string):
        print("My name is ", string)  # or print("My name is "+ string)


Employee.print_good("Diwakar ")

# -------------------------------------------------------------------------

class student:
    @staticmethod
    def Enter_your_name(string):
        print("Your name is " + string)


a = input("Enter your name here : ")
student.Enter_your_name(a)
