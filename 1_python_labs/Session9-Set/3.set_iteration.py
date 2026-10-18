print("------------- accessing set items : ony through loop -------------")

myset = {'mango', 'apple', 'banana', 'gauva', 'cherry', 'kiwi', 'pomegranate'}

for i in myset:
    print(i,end=" ")
print("\n")

print("------------- total items in set: len(myset) -------------")
print(len(myset))

print("---------- check item present in list - in, not in operators ----------")

print('yes, apple is in set') if 'apple' in myset else print('no, apple is not in set')
myset.add('grapes')
{print('no'),print('grapes not in the set')} if ('grapes' not in myset) else {print('yes'), print('grapes is in set')}

print(len(myset))

print("---------- list comparison ----------")
myset1 = {1,2,3,4,5,6}
myset2 = {1,2,3,4,5,6,8,9}

print('equal sets') if myset1 == myset2 else print("not equal sets")