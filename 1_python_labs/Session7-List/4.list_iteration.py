print("---------- Iterating through the list  ----------")
mylist = ['mango', 'apple', 'gauva', 10, 30, 50, True]

for i in mylist:
    print(i,end=" ")
print("\n")

print("---------- print length of list  ----------")
print("length of the list is ",len(mylist))

print("---------- check item present in list - in, not in operators ----------")

print('yes') if 'apple' in mylist else print('no')
mylist.insert(3,'kiwi')
{print('no'),print('kiwi not in the list')} if 'kiwi' not in mylist \
    else {print('yes'), print('kiwi is in list')}

print("---------- list comparison ----------")
mylist1 = [1,2,3,4,5,6]
mylist2 = [1,2,3,4,5,6,8,9]

print('equal lists') if mylist1 == mylist2 else print("not equal lists")