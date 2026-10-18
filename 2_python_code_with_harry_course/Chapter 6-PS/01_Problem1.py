# Write a program to find the greatest of four numbers entered by the user

def get_max_number():
    numbers = []
    for i in range (1,5):
        number = int(input(f"please enter number {i}: "))
        numbers.append(number)
    print(numbers)
    return max(numbers)

print(get_max_number())