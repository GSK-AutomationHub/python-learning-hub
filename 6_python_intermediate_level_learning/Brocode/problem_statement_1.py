temp_list = [3,3,3,5,5,5,5,5,9,9,9,9,9,9,12,12,12,12,12,12,15,15]

from collections import Counter

my_counter = Counter(temp_list)
temp_dict = dict(my_counter)
print(temp_dict)
sorted_dict = sorted(temp_dict.items(), key=lambda x: x[0], reverse=True )
print("sorted dict: ", list(sorted_dict))
filtered_dict = filter(lambda x:x[1] > 5, temp_dict.items())
print("filtered dict: ",list(filtered_dict))


import time

def counter(start=0, stop=0):
    counter_start_time = time.perf_counter()
    for x in range(start, stop+1):
        print(x)
        time.sleep(1)
    print('DONE!')
    counter_end_time =  time.perf_counter()
    counter_time = counter_end_time - counter_start_time
    print(f"The counter duration was: {counter_time:.2f} seconds")

counter(5, 10)

