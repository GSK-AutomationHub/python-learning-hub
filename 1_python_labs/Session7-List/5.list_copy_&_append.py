print("--------- copying the list - list(list), list.copy() ---------")
mylist1 = [1,2,3,4,5]
mylist2 = ['apple', 'mango','chiku']

print("mylist3 = list(mylist1) : copies mylist1 to mylist3")
mylist3 = list(mylist1)
print(mylist3)
mylist3.clear()

print("mylist3 = mylist2.copy() : copies mylist2 to mylist3")
mylist3 = mylist2.copy()
print(mylist3)

print("Loop can be used to copy list1 item to list2")
mylist4 = list()
for i in mylist3:
    mylist4.append(i)
print(mylist4)

print("--------- joining the list using + operator, list.extend(list) ---------")

print("mylist5 = mylist1 + mylist2 : simply concatenate mylist1, mylist2 & add result to mylist4")
mylist5 = mylist1 + mylist2
print(mylist5)

print("mylist6.extend(mylist5) : extends mylist6 with mylist5")
mylist6 = [True, False]
mylist6.extend(mylist5)
print(mylist6)

