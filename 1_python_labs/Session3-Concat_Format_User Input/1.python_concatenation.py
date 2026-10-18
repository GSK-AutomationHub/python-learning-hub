'''
concatenation simply means 'joining' , + sign used as concatenation operator
Imp - concatenation only possible on same data types, it gives error if applied
on variables of different data types
'''

print(10 + 20)     # valid as both values are of int type
print(10 + 10.5)   # valid as int & float addition
print(True + 5)    # valid as True as default value as 1
print(5 + False)   # valid as False as default value as 0

try:
    print(5 + 'ten') # invalid as values are of int & str type
    print('welcome' + 10.5) # invalid as values are of str & float type
    print(True + 'India') # invalid as values are of boolean & str type
except Exception as e:
    print(e)