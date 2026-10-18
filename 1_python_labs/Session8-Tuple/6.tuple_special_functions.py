
a = (1,2,3,4,9,9,7,12,14,15)
b = (1,2,3,4,9,[9,7,12],14,15)

for i,item in enumerate(a):
    print(f"index {i} = {item}")

print(f"value 9 appears {a.count(9)} times in tuple a")
print(f"value 14 is at index {a.index(14)} in tuple a")
print(f"value at index 2 in list nested inside tuple b is {b[5][2]}")
print(f"minimum vale in tuple a is {min(a)}")
print(f"maximum value in tuple a is {max(a)}")
print(f"sum of all tuple items is {sum(a)}")

# functions not supported in tuple
# a.sort()
# print("sorted tuple is ", a)
# a.reverse()
# print("reversed tuple is ", a)