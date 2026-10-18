'''
Write a python program to print the contents of a directory using the os module.
Search online for the function which does that
'''

import os

# Specify the directory you want to list
directory_path = 'C:\\Users\\Ganesh\\Documents\\SDET'

# List all files & directories in specified path
content = os.listdir(directory_path)

# Print each file & directory name
for item in content:
    print(item)
