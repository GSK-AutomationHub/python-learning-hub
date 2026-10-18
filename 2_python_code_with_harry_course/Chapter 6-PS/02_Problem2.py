# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

def get_exam_result():

    sub_marks = []

    for i in range(1, 4):
        mark = int(input(f"Please enter subject marks {i}: "))
        sub_marks.append(mark)
    
    print(sub_marks)

    total_percentage = round((sum(sub_marks)/3), 2)
    print(total_percentage)

    sub_marks_cut_off = []

    for i in range(len(sub_marks)):
        if sub_marks[i] < 33:
            sub_marks_cut_off.append(False)
        else:
            sub_marks_cut_off.append(True)
    
    print(sub_marks_cut_off)

    if False in sub_marks_cut_off or total_percentage < 40:
        print("Failed")

    else:
        print("Passed")


print(get_exam_result())