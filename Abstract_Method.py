from abc import ABC, abstractmethod    # If you want to use a function in all the classes then there is a simple way do do so,
                                                                   # Just we need to use the abstract method, to run a function to all the derived classes
                                                                   # all we need to do is to, import the ABC and abstractmethod from abc module.

class shape(ABC):
    @abstractmethod   # This decorator will forcefully imply this print_area function to all the derived classes. If any class does not make a print_area
                                     # function, then python will raise a error to make a print_area function because it is a part of a abstractmethod.
                                     # By chance if we not need to make print_area function in a class the simply make the function just leave it empty by writing 'pass'.
    def print_area(self):
        return 0

class Rectangle(shape):
    type = "Rectangle"
    sides = 4

    def __init__(self, length, breadth):
        self.length = int(length)  # By default it is of string(str) type so firstly we need to convert it into integer(int) type
        self.breadth = int(breadth)     # By default it is of string(str) type so firstly we need to convert it into integer(int) type

    def print_area(self):
        return self.length * self.breadth

length1 = input("Enter the Length of the Rectangle : ")
breadth1 = input("Enter the Breadth of the Rectangle : ")
rect1 = Rectangle(length1, breadth1)
print(rect1.type)  # This will show an error if print_area function will not be in the Rectangle class
print("The area of the Rectangle is ", rect1.print_area())  # This will print the area of the rectangle.
