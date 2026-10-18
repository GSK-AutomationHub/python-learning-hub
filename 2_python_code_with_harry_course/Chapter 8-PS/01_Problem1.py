# Write a program using functions to find greatest of three numbers

def get_greatest_number():
    numbers = []
    number = int(input(f"Please neter number {1}: "))
    numbers.append(number)
    print(numbers)
    return max(numbers)

print(f"the greatest number of entered numbers is {get_greatest_number()}")
