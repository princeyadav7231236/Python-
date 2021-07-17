class base1:
    @staticmethod
    def name(name):
        print("Your name is ", name)
class base2:
    @staticmethod
    def class_(class_name):
        print("Your class is ", class_name)
class base3(base1, base2):
    @staticmethod
    def section(sec):
        print("Your section is ", sec)

obj1 = base3()
name1 = input("Enter your name : ")
class1 = input("Enter your class here : ")
sec1 = input("Enter your section : ")
obj1.name(name1)
obj1.class_(class1)
obj1.section(sec1)
