class A:
    class_var1 = "I am a class variable in class A "

    def __init__(self):
        self.var = "I am inside class A's Constructors"
        self.class_var1 = "Instance variable in class A "


class B(A):
    class_var1 = "I am in class B"

    def __init__(self):
        self.var = "I am inside class B's Constructor"
        self.class_var1 = "Instance variable in class B"
        super().__init__()   # This super function will set the constructor of parent class.
        print(super().class_var1)   # This will print the value of class_var1 of parent class. because, super function is called.


a = A()
b = B()
print(b.var, "\n", b.class_var1)
