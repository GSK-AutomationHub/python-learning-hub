'''
list [] - list is collection which store multiple items in single variable
 - Ordered : list items always get stored in particular order / sequence [starting with index 0]
 - Changeable / mutable - list items can be added/deleted/modified
'''

print("------------- declaring the list -------------")
mylist1 = [1, 2, 3, 4, 5]
print("mylist1 is list having number items", mylist1)
mylist2 = ['mango', 'apple', 'banana', 'gauva', 'cherry', 'kiwi', 'pomegranate']
print("mylist2 is string list", mylist2)
mylist3 = ['apple', 10, True]
print("mylist3 have diff data types items ", mylist3)
mylist4 = list()  # or by [] - declaring empty list
print("mylist4 is empty list declared as list()", mylist4)
print(type(mylist4))

print("------------- accessing list items -------------")
mylist5 = ['mango', 'apple', 'banana', 'gauva', 'cherry', 'kiwi', 'pomegranate']
print("accessing item at 3rd index from mylist5 -", mylist5[3])
print("accessing item at 5th index from mylist5 -", mylist5[5])

print("------------- unpacking list items -------------")
mylist5 = ['mango', 'apple', 'banana', 'gauva', 'cherry', 'kiwi', 'pomegranate']
a,b,c,d,e,f,g = mylist5
print (a,b,c,d,e,f,g)


