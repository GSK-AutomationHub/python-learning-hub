print("---------------- string concatenation (+)  & duplication (*) ---------------- ")
str1 = 'welcome'
print(str1 + ' world of python')  # concatenation of strings using + operator

str2 = 'Jay ShriRam! '
print(str2 * 3)  # printing string multiple times (duplication) using * operator

print("---------------- string slicing ---------------- ")
str3 = "hum hum hansarupam, ramdutam namami"
print(str3)
print("# str3[20:28] : string slice with ST 20 & EI as n-1 i.e. 27 ")
print(str3[20:28])
print("# str3[:28] : string slice with ST as 0 as no SI mention & EI as n-1 i.e. 27 ")
print(str3[:28])
print("# str3[1:18] : string slice with ST  1 & EI as n-1 i.e. 17 ")
print(str3[1:18])
print("# str3[8:] : string slice with ST as 8 & EI as last index as no EI mention ")
print(str3[8:])
print("# str3[1:-1] : remove last index ")
print(str3[1:-1])
print("# str3[1:-2]) : remove last 2 indexes ")
print(str3[1:-2])
