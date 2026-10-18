'''
dict {key:value} - dict is collection which store items in key value pair format
 - 'Key' is always unique in dict, value can repeat
 - Unordered : dict items never get stored in particular order / sequence
 - Un-Indexed : dict items never indexed
 - Changeable / mutable - dict items can be added/deleted/modified
'''

print("------------- declaring the dict -------------")
mydict = {}  # declaring empty dict
print("mydict is empty dict declared as dict{}- ", mydict)
print(type(mydict))
mydict= {
    'Name':'Rahul',
    'Roll No':123,
    'School':'Gajanan Public Highscool',
    'is_scholar': True
}
print(mydict)


print("------------- total items in dict: len(mydict) -------------")

print(len(mydict))


