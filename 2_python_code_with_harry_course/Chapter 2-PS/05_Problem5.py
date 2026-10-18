# Write a python program to find an average of two numbers entered by the user

import random

def get_avg_number(num1, num2):
    return int((num1+num2)/2)


num1, num2 = random.randint(1,100), random.randint(1,100)
print(num1, num2)

print(get_avg_number(num1, num2))
