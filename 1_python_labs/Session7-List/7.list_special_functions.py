
a = [1,2,3,4,9,9,7,12,14,15]
b = [1,2,3,4,9,[9,7,12],14,15]

for i,item in enumerate(a):
    print(f"index {i} = {item}")

print(f"value 9 appears {a.count(9)} times in list a")
print(f"value 14 is at index {a.index(14)} in list a")
print(f"value at index 2 in list nested inside list b is {b[5][2]}")
print(f"minimum vale in list a is {min(a)}")
print(f"maximum value in list a is {max(a)}")
print(f"sum of all list items is {sum(a)}")

a.sort()
print("sorted list is ", a)
a.reverse()
print("reversed list is ", a)

print(" ------------------- converting List to String -------------------- ")
abc = ["value", "at", "index", "2" ]
abc_str = ",".join(abc)
abc_str = abc_str.replace(","," ")
print(abc, abc_str)