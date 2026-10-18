def count_up_to(number):
    count = 1
    while count <= number:
        yield count
        count +=1

number = int(input("Please enter the number you want to count up to: "))
counter = count_up_to(number)

print(next(counter))
# print(next(counter))
# print(next(counter))

import time
print("-------------------generator with for loop () -------------------------")
for count in counter:
    print(count)
    time.sleep(0.5)

print("------------------ generator expression () --------------------------")

sqaure = (x**2 for x in range(1,6))
print(next(sqaure))
print(next(sqaure))
print(list(sqaure))