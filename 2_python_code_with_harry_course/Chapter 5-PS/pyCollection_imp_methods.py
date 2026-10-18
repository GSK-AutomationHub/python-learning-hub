
# list oof lists
marks = [['Harry',90],['Lorry',60],['amy',75]]


# enumerate to iterate over list with index & value
for index, value in enumerate(marks):
    print(f"marks[{index}] ={value}")


#list to dictonaries
marks_dict = dict(marks)
print(marks_dict)

list_1 = ['Harry','Lorry', 'Amy']
list_2 = [90, 60, 75]

print("list to dict using zip --> ", dict(zip(list_1,list_2)))

# dictonary methods
print(marks_dict.items())
print(marks_dict.keys())
print(marks_dict.values())
marks_dict.get("Harry2") # returns None
#marks_dict["Harry2"] # gives key error


# list to string using - delimiter.join(list)
mark_list = marks_dict.keys()
marks_str = ",".join(mark_list)
print(marks_str)


# string to list using - split(delimiter)
print(marks_str.split(','))


# list to set
fruit_list_1 = ['mango','cherry', 'apple','mango']
fruit_list_2 = ['mango','apple', 'watermelon','muskmelon']

print(set(fruit_list_1),set(fruit_list_2))

# # set methods
print(set(fruit_list_1).intersection(set(fruit_list_2)))
print(set(fruit_list_1) & (set(fruit_list_2)))
print(set(fruit_list_1).union(set(fruit_list_2)))
print(set(fruit_list_1) | (set(fruit_list_2)))
print(set(fruit_list_1).difference(set(fruit_list_2)))
print(set(fruit_list_1) - (set(fruit_list_2)))
print(set(fruit_list_1).symmetric_difference(set(fruit_list_2)))
print(set(fruit_list_1) ^ (set(fruit_list_2)))


s1 = {3,6,9,12,15,18}
s2 = {12, 15, 18}

print(s2.issubset(s1))
print(s1.issuperset(s2))