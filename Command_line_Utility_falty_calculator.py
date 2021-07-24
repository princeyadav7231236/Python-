import argparse
import sys

def faulty_calculator(string):
    if string.a == "add" and string.x == 56 and string.y == 9:
        return 77

    elif string.a == "mul" and string.x == 45 and string.y == 3:
        return 555

    elif string.a == "div" and string.x == 56 and string.y == 6:
        return 4

    elif string.a == "add":
        return string.x + string.y

    elif string.a == "sub":
        return string.x - string.y

    elif string.a == "mul":
            return string.x * string.y

    elif string.a == "div":
            return string.x / string.y


if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument("--x", type=float, default=1.0, help="Enter the First number ")
    parse.add_argument("--y", type=float, default=1.0, help="Enter the Second number ")
    parse.add_argument("--a", type=str, help="Enter the Operator ")

    arguments = parse.parse_args()
    sys.stdout.write(str(faulty_calculator(arguments)))

