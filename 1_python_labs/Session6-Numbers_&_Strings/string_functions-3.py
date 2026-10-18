print("---------- string in, not in operators, returns boolean output --------- ")
str = "welcome"

print('come' in str)
print('ok' in str)

print('come' not in str)
print('ok' not in str)

print("---------------- searching for sub-string ---------------- ")
str1 = 'welcome to world of python'

print(str1.startswith('welcome'))
print(str1.endswith('thon'))
print(str1.find('world'))  # if found function returns index of first charc
print(str1.find('ok'))  # if not found function returns -1
print(str1.count('o'))  # count function returns no of time charc/world/phrase appears in string



