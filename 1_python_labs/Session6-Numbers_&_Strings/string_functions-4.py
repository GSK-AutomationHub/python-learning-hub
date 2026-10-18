print("---------------- string checks ---------------- ")
str = 'India2025'

print(str.isupper())
print(str.islower())
print(str.isalnum())
print(str.isalpha())
print(str.isdigit())
print(str.isidentifier())
print(str.isspace())

print("---------------- converting string ---------------- ")
str1 = 'Welcome to Python'
print(str1.title())
print(str1.upper())
print(str1.lower())
print(str1.swapcase())

print("---------------- string strip(), split(), replace() ---------------- ")

print("function 'strip' trims or removes leading / trailing spaces from string")
str4 = "    arjun & krishan    "
print(str4.lstrip())
print(str4.rstrip())
print(str4.strip())

print("function 'split' converts 'string' into 'list' as per delimiter specified")
str3 = "Mushkil Wqkt, Camondo Sqkt"
a= str3.split(',')
print("after using 'split' function on string str3, result is as below\n", a)

print("function 'replace' change string value/ delimiter specified in string")
str3 = "Mushkil Wqkt, Camondo Sqkt"
a= str3.replace(',','|')
print("after using 'replace' function on string str3, result is as below\n", a)

