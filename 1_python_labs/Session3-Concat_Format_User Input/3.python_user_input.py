# function input() used to take input from use,
# functions int(), float() used for type casting

firstname = input("please enter your firstname: ")
lastname = input("please enter your lastname: ")
salary = float(input("please enter your current salary: "))

print(f'employee {firstname} {lastname} have current salary {salary}')

num1 = input("enter first number: ")
num2 = input("enter second number: ")
print(num1 + num2)  # this will give wrong result as user input will be in default str type
print(type(num2))
print(type(num2))

print(int(num1) + int(num2))  # this is correct way to type cast user input before processing
