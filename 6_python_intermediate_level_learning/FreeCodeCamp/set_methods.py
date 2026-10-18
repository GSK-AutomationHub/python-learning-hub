my_set1 = set([1,2,3,4,5,6,7,8,9,0])
my_set2 = set([2,4,6,8,10])

# union
print(my_set1 | my_set2)

# intesection
print(my_set1 & my_set2)

# difference
print(my_set1 - my_set2)

# symmetric difference
print(my_set1 ^ my_set2)

# update
my_set2.update([12,14,16])
print(my_set2)

print("--------------------------------------------------")

print(my_set2.symmetric_difference_update(my_set1))
print(my_set2)

