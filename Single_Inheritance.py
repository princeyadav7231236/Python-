class Parent:
    @staticmethod
    def first(self):
        print("Parent function")

class child(Parent):   # In this child class is Inheriting all the methods and functions of the parent class
    @staticmethod
    def second():
        print("Child Function")

obj1 = child()
child.first(obj1)
child.second()
