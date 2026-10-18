print("------------- accessing dict items  -------------")

mydict= {
    'Name':'Rahul',
    'Roll No':123,
    'School':'Gajanan Public Highscool',
    'is_scholar': True
}

print("# mydict['Key'] & mydict.get('Key') : To access dict value")
print(mydict['Name'])
print(mydict.get('School'))

print("------------- unpacking dict items -------------")
d = {
    "name": "Amit",
    "role": "Automation Lead",
    "salary": 6000000
}

name_key,role_key,salary_key = d.keys()
print(name_key,role_key,salary_key)

name_value,role_value,salary_value = d.values()
print(name_value,role_value,salary_value)


print("---------- adding item to dict ----------")

print("# mydict['New Key'] = 'value' : To add item to dict")
mydict['Grade'] = 'A+'
mydict['Social'] = 'NCC Cadet'
mydict['Interest'] = 'Swimming, Football'
print(mydict)

print("---------- changing the dict value ----------")

print("# mydict['Key'] = 'new value' : To change dict value")
mydict['Name'] = 'Rohit'
mydict['School'] = 'Gajanan Maharaj Public School'
print(mydict)

mydict.update({"Name":"Ratan", "Teacher":"Govinda"})
print(mydict)

print("--------- removing item from dict  ---------")

print("mydict.pop('key') : removes item in dict")
mydict.pop('Social')
print(mydict)

print("del mydict['key'] : removes item in dict")
del mydict['Interest']
print(mydict)

print("mydict.clear() cleans the dict i.e. empty the dict")
mydict.clear()
print(mydict)

print("--------- deleting dict - del mydict ---------")
del mydict
try:
    print(mydict)
except Exception as e:
    print(e)
