# Write a python function to print first n lines of the following pattern:
'''
***
** - for n = 3
*
'''

def print_design(n=0):
    while n > 0:
        print("*" * n)
        n-=1

def print_design_reverse(n=0):
    i=n-1
    while i > 0:
        print("*" * (n-i))
        i-=1
        

print_design(10)
print("-----------------------------------")
print_design_reverse(10)