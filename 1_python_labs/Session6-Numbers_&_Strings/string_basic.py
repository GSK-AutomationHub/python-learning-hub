
print("---------------- string declaration ---------------- ")
str1 = 'welcome'  # or str1 = "welcome"
print('str1 = "welcome"')
str2 = str("to python")  # or str('to python')
print("str2 = str('to python')")

print("---------------- creating empty strings ---------------- ")
# empty string declaration
str3 = ''  # or st3 = ""
print('str3 = ""')
str4 = str()
print('str4 = str()')

print("---------------- printing the strings ---------------- ")
print(str1, str2, str3, str4)

print("---------------- id() - returns memory location of string object ---------------- ")
str5 = 'Jay Ho !'
print(f'string {str5} is stored at memory address {id(str5)}')

print("---------------- strings are immutable ---------------- ")
str_note1 = 'original str5 object has not changed its identity i.e. it not got modified at place'
print(str_note1)
print(id(str5))
str_note2 = 'but new str5 type object created for modified content at different memory location'
print(str_note2)
str5 = str5 + " Maharaj"
print(str5)
print(id(str5))

