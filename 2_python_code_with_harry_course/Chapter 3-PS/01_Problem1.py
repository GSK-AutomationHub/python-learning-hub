# Write a python program to display a user entered name followed by Good 
# Afternoon using input () function


def greetings(user_name):
    print(f"Hello {user_name}, Good Afternoon!")
    print("Hello {}, Good Afternoon!" .format(user_name))


user_name = input("Please enter your name - ")

greetings(user_name)
