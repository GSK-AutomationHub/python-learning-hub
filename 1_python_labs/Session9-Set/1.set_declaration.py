'''
set {} - set is collection which store multiple items in single variable
 - Unordered : set items never get stored in particular order / sequence 
 - Un-Indexed : set items never indexed 
 - Changeable / mutable - set items can be added/deleted/modified
'''

print("------------- declaring the set -------------")
myset1 = {1, 2, 3, 4, 5}
print("myset1 is set having number items", myset1)
myset2 = {'mango', 'apple', 'banana', 'gauva', 'cherry', 'kiwi', 'pomegranate'}
print("myset2 is string set", myset2)
myset3 = {'apple', 10, True}
print("myset3 have diff data types items ", myset3)
myset4 = set()  # declaring empty set
print("myset4 is empty set declared as set()- ", myset4)
print(type(myset4))

print("------------- total items in set: len(myset) -------------")

print(len(myset2))

print("------------- unpacking set items -------------")
myset5 = {'mango', 'apple', 'banana', 'gauva', 'cherry', 'kiwi', 'pomegranate'}
a,b,c,d,e,f,g = myset5
# Order of assignment is random
print (a,b,c,d,e,f,g)

