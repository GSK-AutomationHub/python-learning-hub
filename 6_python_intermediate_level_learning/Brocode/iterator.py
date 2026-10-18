import time
from itertools import count, cycle, repeat

# my_list = list(range(10))

# print(my_list)
# for i in my_list:
#     print(i)
#     time.sleep(0.5)

def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter()
        func(*args,**kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"function execution time = {execution_time:.2f} seconds")
    return wrapper


@timer
def counter(no):
    for item in count(no):
        print(item)
        time.sleep(0.5)
        if item == 12:
            break


counter(3)