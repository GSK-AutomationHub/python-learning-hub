'''
tuples are Immutable
- i.e. tuple items can not be manipulated with add/edit/delete operations
- so tuple do not support directly to the functions like
    - tuple[i]=v, append(v), insert(i,v), pop(i), remove(v), clear()
    - If applied these function on tuple it gives TypeError
- Workaround - Convert tuple to list, do manipulation & convert back list to tuple
'''

print("----------------- Workaround for tuple manipulation -------------------")

mytuple = ('mango', 'apple', 'banana', 'gauva', 'cherry', 'kiwi', 'pomegranate')

print("------- # Step 1: Convert tuple into list -------")
print("mylist = list(mytuple) : Converts tuple to list")
mylist = list(mytuple)
print(mylist)
print("------- # Step 2: manipulate the list items -------")
mylist.append('chiku')
mylist.insert(3,'dragon fruit')
mylist[4] = 'orange'
mylist.pop(5)
mylist.remove('apple')
print(mylist)
print("------- # Step 3: Convert the list back to tuple -------")
mytuple = tuple(mylist)
print(mytuple)




