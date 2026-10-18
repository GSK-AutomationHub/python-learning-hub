mydict = {
    'Name': 'Rohit',
    'Roll No': 123,
    'School': 'Gajanan Maharaj Public School',
    'is_scholar': True,
    'Grade': 'A+',
    'Social': 'NCC Cadet',
    'Interest': 'Swimming, Football'
}

print("------------- total items in dict: len(mydict) -------------")

print(len(mydict))

print("------------- accessing dict items : loop -------------")

print("-------- printing dict keys : normal loop, mydict.keys() -------------")

for i in mydict:
    print(i, end=" ")
print("\n")

for i in mydict.keys():
    print(i, end=" ")
print("\n")

print("-------- printing dict values : loop with mydict[i], mydict.values() ---------")

for i in mydict:
    print(mydict[i], end=" ")
print("\n")

for i in mydict.values():
    print(i, end=" ")
print("\n")

print("-------- printing dict key & values : loop with i : mydict[i], mydict.items() ---------")

for i in mydict:
    print(i, mydict[i], end=" ")
print("\n")

for i,j in mydict.items():
    print(i, j, end=" ")
print("\n")

print("---------- check item present in list - in, not in operators ----------")

print('yes, School is in dict') if 'School' in mydict else print('no, School is not in dict')

{print('no'), print('Grade not in the dict')} if 'Grade' not in mydict \
    else {print('yes'), print('Grade is in dict')}


