# Write a program to accept marks of 6 students and display them in a sorted manner

def get_student_sorted_marks():
    student_marks = []
    for i in range(1,7):
        student_marks.append(int(input(f"please enter mark for student no {i}: ")))
    student_marks.sort()
    return student_marks

print(get_student_sorted_marks())
