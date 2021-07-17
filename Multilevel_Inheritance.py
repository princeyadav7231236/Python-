# Syntax :
# class parent:
#     pass
# class derived_1(parent):
#     pass
# class derived_2(derived_1):
#     pass
# ---------------------------------------------------
# This is an example of Multilevel Inheritance
class level1:
    def first(self):
        print("Hey How're you?")


class level2(level1):
    def second(self):
        print("Yoo what's upp !")


class level3(level2):
    def third(self):
        print("Hello World !!!")


obj1 = level3()
obj1.first()
obj1.second()
obj1.third()
