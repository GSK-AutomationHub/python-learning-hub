# Approach-1, creating temp string & loop
str = 'welcome'
rev_str = ''

for i in str:
    rev_str = i + rev_str
    print(rev_str)
print(f'original string is {str}, reversed string is {rev_str}')

# Approach-2, using slicing technique
print(str[::-1])
