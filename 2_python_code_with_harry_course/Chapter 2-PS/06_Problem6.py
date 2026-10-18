# Write a python program to calculate the square of a number entered by the user

import random

def get_square_or_cube_of_no(number,pow):
    return number**2 if pow==2 else number**3


number = random.randint(1, 50)
print(number)

print(get_square_or_cube_of_no(number,3))