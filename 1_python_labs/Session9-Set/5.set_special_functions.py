'''
set has below special functions
union --> to join two sets
intersections --> to get common values from sets
difference --> to get not matching values from set 1 w.r.t set 2
symmetric difference --> to get not matching values from both set 1 & set 2
Operators used in set operations
   - Union ==> (set1 | set2), set1.union(set2)
   - Intersection ==> (set1 & set2), set1.intersection(set2)
   - Difference ==> (set1 - set2), set1.difference(set2)
   - Symmetric Difference ==> (set1 ^ set2), set1.symmetric_difference(set2)
issuperset - if set1 has all values present in set2, then set1 suer set
issubset - in above case set2 is subset of set1
'''

myset1 = {'apple', 'banana', 'mango', 'chiku', 'papaya'}
myset2 = {'apple','papaya','blue cherry','grapes','anjir'}


common_fruits = myset2.intersection(myset1)
print("common fruits in both sets are -", common_fruits)

different_fruits = myset2.difference(myset1)
print("different fruits in set2 are -", different_fruits)

all_fruits = myset1.union(myset2)
print("all fruits from both sets are -", all_fruits)

uncommon_fruits = myset2.symmetric_difference(myset1)
print("uncommon fruits in both sets are -",uncommon_fruits)

print("is all_fruits superset of myset2?", all_fruits.issuperset(myset2))

print("is myset2 subset of all_fruits?",myset2.issubset(all_fruits))

print("------------------------------------------------------------------------------------")

a = {2,4,6,8,12}
b = {2,5,6,10,12}

# | --> Union, & --> Intersection, - --> difference, ^ --> symmetric difference
print(f"union of set a and set b is \n{a.union(b)}")
print(f"union of set a and set b is \n{a | b}")

print(f"intersection of set a and set b is \n{a.intersection(b)}")
print(f"intersection of set a and set b is \n{a & b}")

print(f"difference of set a from set b is \n{a.difference(b)}")
print(f"difference of set a from set b is \n{a - b}")

print(f"difference of set b from set a is \n{b.difference(a)}")
print(f"difference of set b from set a is \n{b - a}")

print(f"symmetric difference of set a and set b is \n{a.symmetric_difference(b)}")
print(f"symmetric difference of set a and set b is \n{a ^ b}")
