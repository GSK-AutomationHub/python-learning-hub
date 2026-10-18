# problem statement : to check exam result by taking exam no user input

def check_exam_result():
    name = input("please enter your name: ")
    exam_no = input("please enter your exam number: ")
    {print(f"Welcome {name}"),print("congrates, you cracked it!")} if exam_no.__contains__('batch3') else {print(f"Welcome {name}"),print('better luck next time')}

def even_number_check(num):
    print(f"{num} is an even number") if num % 2 == 0 else print(f"{num} is odd number")


check_exam_result()
even_number_check(6)

