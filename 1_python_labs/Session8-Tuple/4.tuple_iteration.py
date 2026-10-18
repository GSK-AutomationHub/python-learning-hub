print("---------- Iterating through the list  ----------")
mytuple = ('mango', 'apple', 'gauva', 10, 30, 50, True)

for i in mytuple:
    print(i,end=" ")
print("\n")

print("---------- print length of list  ----------")
print("length of the list is ",len(mytuple))

print("---------- check item present in list - in, not in operators ----------")

print('yes') if 'apple' in mytuple else print('no')
{print('no'),print('kiwi not in the list')} if 'kiwi' not in mytuple \
    else {print('yes'), print('kiwi is in list')}

print("---------- tuple comparison ----------")
mytuple1 = (1,2,3,4,5,6)
mytuple2 = (1,2,3,4,5,6,8,9)

print('equal tuples') if mytuple1 == mytuple2 else print("not equal tuples")