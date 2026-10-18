print("--------- copying the tuple ------------")
mytuple1 = (1,2,3,4,5)
mytuple2 = ('apple', 'mango','chiku')
print("tuple1 = tuple2 : copies the tuple2 in tuple1")
mytuple3 = mytuple2
print(mytuple3)

print("--------- joining the tuple using + operator ---------")

print("mytuple5 = mytuple1 + mytuple2 : simply concatenate mytuple1, mytuple2 & add result to mytuple4")
mytuple5 = mytuple1 + mytuple2
print(mytuple5)

print("--------- deleting the tuple ------------")

print("del keyword is used to delete tuple")
del mytuple5
try:
    print(mytuple5)
except Exception as e:
    print(e)