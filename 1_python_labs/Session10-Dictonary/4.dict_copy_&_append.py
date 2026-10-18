print("--------- copying the dict ------------")
mydict1 = {
    'Name':'Rahul',
    'Roll No':123,
    'School':'Gajanan Public Highscool',
    'is_scholar': True
}
mydict2 = {}
mydict3 = {}
print("# dict2 = dict1 : copies the dict1 in dict2")
mydict2 = mydict1
print(mydict2)

print("# dict3 = dict2.copy() : copies dict2 to dict1 using copy() function")
mydict3 = mydict2.copy()
print(mydict3)

