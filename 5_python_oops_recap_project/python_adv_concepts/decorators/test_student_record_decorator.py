

def student_record_decorator(some_func):
    def wrapper_function(name, id, division, exam_score):
        print("Welcome to Modern English School, Pune")
        print("Below is your exam result ... ")
        print(some_func(name, id, division, exam_score))
        print("Thanks for visiting Modern English School Website")
    return wrapper_function

@student_record_decorator
def student_record(name:str, id:str, division:str, exam_score:float):
    return {'name': name, 'id': id, 'division': division, 'exam_score':exam_score}

student_record('Vijay Kumar', 'Std-1234', '10th-A', 72.50)