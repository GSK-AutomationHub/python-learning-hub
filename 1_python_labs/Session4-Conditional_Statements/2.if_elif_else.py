# problem statement : print day name based on day number input
def print_day_name():
    day_number = int(input("please enter day number: "))

    if day_number == 1:
        print("Monday")
    elif day_number == 2:
        print("Tuesday")
    elif day_number == 3:
        print("Wednesday")
    elif day_number == 4:
        print("Thursday")
    elif day_number == 5:
        print("Friday")
    elif day_number == 6:
        print("Saturday")
    elif day_number == 7:
        print("Sunday")
    else:
        print("Invalid day number")

# problem statement : print max of three numbers submitted
def get_max_num(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            print(f'{num1} is greater number')
        else:
            print(f'{num3} is greater number')
    elif num2 > num3:
        print(f'{num2} is greater number')
    elif num2 == num3:
        print("It seems numbers are matching")
    else:
        print(f'{num3} is greater number')

# function call
print_day_name()
get_max_num(24, 24, 24)
