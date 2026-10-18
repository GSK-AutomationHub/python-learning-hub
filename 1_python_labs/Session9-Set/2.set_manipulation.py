print("------------- accessing set items : ony through loop -------------")

myset = {'mango', 'apple', 'banana', 'gauva', 'cherry', 'kiwi', 'pomegranate'}

for i in myset:
    print(i,end=" ")
print("\n")

print("---------- adding item to set - add(), update() ----------")

print("myset.add('value') adds one value to in set")
myset.add('chiku')
print(myset)

print("myset.update(['value1,'value2']) update adds multiple values to in set" )
myset.update(['grapes','dragon fruit'])
print(myset)

print("--------- removing item from set - remove(V), discard(), clear() ---------")

print("myset.remove() removes item in set")
myset.remove('kiwi')
print(myset)
print("remove function returns KeyError for value not present in set")
try:
    myset.remove('abc')
except Exception as e:
    print(e)

print("myset.discard() also removes item in set")
myset.discard('dragon fruit')
print(myset)
print("discard function does not return error for value not present in set")
myset.discard('abc')
# try:
#     myset.discard('abc')
# except Exception as e:
#     print(e)

print("myset.clear() cleans the set i.e. empty the set")
myset.clear()
print(myset)

print("--------- deleting set - del myset ---------")
del myset
try:
    print(myset)
except Exception as e:
    print(e)