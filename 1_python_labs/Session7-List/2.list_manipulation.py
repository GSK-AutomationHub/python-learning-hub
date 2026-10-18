print("---------- adding item to list - append(), insert() ----------")

mylist = ['mango', 'apple', 'banana', 'gauva', 'cherry', 'kiwi', 'pomegranate']
print("mylist.append('value') adds value to last index in list")
mylist.append('chiku')
print(mylist)

print("mylist.insert(Index,'Value') adds value at specified index in list" )
mylist.insert(3,'dragon fruit')
print(mylist)

print("---------- edit / modify item in list - mylist[I] = V ----------")

print("mylist[3]=orange will modify / overwrite item at 3rd index in list")
mylist[3] = 'orange'
print(mylist)

print("--------- removing item from list - pop(I), remove(V), del, clear() ---------")

print("mylist.pop() removes item at last index in list")
mylist.pop()
print(mylist)

print("mylist.pop(3) removes item at specified index in list")
mylist.pop(3)
print(mylist)

print("mylist.remove('value') removes specified item from the list")
mylist.remove('gauva')
print(mylist)

print("del mylist[I] del keyword removes value at specified index from the list")
del mylist[5]
print(mylist)

print("mylist.clear() cleans the list i.e. empty the list")
mylist.clear()
print(mylist)