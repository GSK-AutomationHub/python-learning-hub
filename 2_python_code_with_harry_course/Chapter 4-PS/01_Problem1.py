# Write a program to store seven fruits in a list entered by the user.


def get_user_fruit_list():
    user_fruit_list = []
    for i in range(1,8):
        user_fruit_list.append(input(f"please enter frount no {i}: "))
    return user_fruit_list

print(get_user_fruit_list())