import os

from os.path import samefile

path=os.getcwd()

# writing to text file
file = open(path+'/samplefile','w')
file.write("first line of the file..\n")
# file.write("second line of the file..\n")
# file.write("third line of the file..\n")
file.close()

# reading from text file
# file = open(path+ '/samplefile','r')
# # print(file.readline())
# print(file.read())

# append content to text file
file = open(path+ '/samplefile','a')
file.write("forth line of the file..\n")
file.write("fifth line of the file..\n")
file.close()
file = open(path+ '/samplefile','r')
print(file.read())