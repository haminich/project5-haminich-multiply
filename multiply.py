# Author: Nicholas Hamilton
# GitHub username: haminich
# Date: 2/9/2023


def multiply(num1, num2):
    if num2 == 0:
        return 0
    elif num2 == 1:
        return num1
    else:
        return num1 + multiply(num1, num2-1)
