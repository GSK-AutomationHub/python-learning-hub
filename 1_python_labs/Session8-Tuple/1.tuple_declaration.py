'''
tuple () - tuple is collection which store multiple items in single variable
 - Ordered : tuple items always get stored in particular order / sequence (starting with index 0)
 - Unchangeable / Immutable - tuple items can not get added/deleted/modified
'''

print("------------- declaring the tuple -------------")
mytuple1 = (1, 2, 3, 4, 5)
print("mytuple1 is tuple having number items", mytuple1)
mytuple2 = ('mango', 'apple', 'banana', 'gauva', 'cherry', 'kiwi', 'pomegranate')
print("mytuple2 is string tuple", mytuple2)
mytuple3 = ('apple', 10, True)
print("mytuple3 have diff data types items ", mytuple3)
mytuple4 = ()  # declaring empty tuple
print("mytuple4 is empty tuple declared as ()- ", mytuple4)
print(type(mytuple4))

print("------------- accessing tuple items -------------")
mytuple5 = ('mango', 'apple', 'banana', 'gauva', 'cherry', 'kiwi', 'pomegranate')
print("accessing item at 3rd index from mytuple5 -", mytuple5[3])
print("accessing item at 5th index from mytuple5 -", mytuple5[5])

print("------------- unpacking tuple items -------------")
mytuple5 = ('mango', 'apple', 'banana', 'gauva', 'cherry', 'kiwi', 'pomegranate')
a,b,c,d,e,f,g = mytuple5
print (a,b,c,d,e,f,g)


