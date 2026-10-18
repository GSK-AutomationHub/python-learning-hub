# Check the type of variable assigned using input () function


def get_variable_type(user_input):
    return type(user_input)

def convert_str_to_int(user_input):
    return int(user_input)

def convert_str_to_float(user_input):
    return float(user_input)

user_input = input("Please enter what's in your mind: ")
user_input = convert_str_to_float(user_input)

print(get_variable_type(user_input))