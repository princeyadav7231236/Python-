import argparse
import sys


def calc(string):
    if string.o == "add":
        return string.x + string.y

    elif string.o == "sub":
        return string.x - string.y

    elif string.o == "mul":
        return string.x * string.y

    elif string.o == "div":
        return string.x / string.y

    else:
        return "Something went Wrong"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=float, default=1.0, help="Enter First number ")
    parser.add_argument("--y", type=float, default=1.0, help="Enter Second number ")
    parser.add_argument("--o", type=str, default="add", help="Enter the Operator ")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))  # This program is now become an utility if we will run this in Windows Powershell Then the program will run
