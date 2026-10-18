# Write a python program to find remainder when a number is divided by z
import random

def get_remainder(num1, num2):
    return num1 % num2 if num1 > num2 else num2 % num1
    # if num1 > num2:
    #     return num1 % num2
    # else:
    #     return num2 % num1

print(get_remainder(random.randint(1,50), 2))