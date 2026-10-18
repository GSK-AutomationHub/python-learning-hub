

result = lambda item : item[::-1]
print(result(987654321))

def reverse_the_number2(user_input):
    reverse_user_input = ''
    str(user_input) if type(user_input) != str else user_input
    for char in range(len(user_input)):
        reverse_user_input = user_input[char] + reverse_user_input
    return reverse_user_input

# print(reverse_the_number2(987654321))