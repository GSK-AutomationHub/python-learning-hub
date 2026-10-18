'''
for loop can be used when we are certain about no of iterations
loop steps --> initialization, condition check, increment / decrement
range() function helps in iterating in specific loop range, usually used in for loop with len() function.
range() iterate from starting index till n i.e. (last index-1)
range syntax - range(start index,end index, increment/decrement count) '''

print('---------------- range() function examples ---------------- ')
# print("\n")
print('---------------- Print number from 0 to 9 ---------------- ')

for i in range(10):  # here iteration starts with 0 till (n-1) i.e. 9
    print(i, end=" ")
print("\n")

print('---------------- Print number from 1 to 10 ---------------- ')

for i in range(1, 11):
    print(i, end=" ")  # here iteration starts from start index 1 till (n-1) i.e. 10
print("\n")

print('---------------- print number 5 to 10 ---------------- ')

for i in range(5, 11):  # here iteration starts from start index 5 till (n-1) i.e. 10
    print(i, end=" ")
print("\n")

print('---------------- print number -10 to -5 ---------------- ')

for i in range(-10, -4):  # here iteration starts from start index -10 till (n-1) i.e. -5
    print(i, end=" ")
print("\n")

print('---------------- print number -10 to -5 with 2 number gap---------------- ')

for i in range(-10, -4, 2):  # here range will iterate from -10 to -4 by decrementing each iteration by 2
    print(i, end=" ")
print("\n")

print('---------------- print number 1 to 10 in descending order ---------------- ')

for i in range(10, 0, -1):  # here range will iterate from 10 to 0 by decrementing each iteration by 1
    print(i, end=" ")
print("\n")

print('---------------- print even number till 30 ---------------- ')

for i in range(2, 30, 2):  # here range will iterate from 0 to 30 by incrementing each iteration by 2
    print(i, end=" ")
print("\n")

print('---------------- print odd number till 30 ---------------- ')

temp_list = []
for i in range(1, 30, 2):  # here range will iterate from 1 to 30 by incrementing each iteration by 2
    temp_list.append(i)
    print(i, end=" ")
print("\n")

print('---------------- print odd number till 30, starting largest 1st ---------------- ')

temp_list.reverse()  # reversed list items

for i in range(len(temp_list)):
    print(temp_list[i], end=" ")

print('---------------- unpacking of range(n) ---------------- ')

a,b,c,d,e = range(5)
print(a,b,c,d,e)

