import math
from os import strerror

num1 = float(input("Enter a nunmber: "))
op = input("Enter operator: ")
num2 = float(input("Enter another number: "))


def calculate():
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "%":
        print(num1 % num2)
    else:
        print("Invalid Operand")


calculate()
