# Write a program to input eight numbers from the user and display all the unique numbers (once).

def display_unique_nos():
    number_set = set()
    for i in range(1,9):
        number_set.add(int(input(f"Please enter your desired value as number {i}: ")))
    return number_set

print(display_unique_nos())

