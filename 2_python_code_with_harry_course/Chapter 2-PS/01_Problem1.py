# Write a python program to add two numbers.

import random

def sum(num1, num2):
    return num1 + num2

no1 = random.randint(1,100)
no2 = random.randint(1,100)

print(f"num1 is {no1}")
print(f"num2 is {no2}")

sum_result = sum(no1, no2)

print(sum_result)