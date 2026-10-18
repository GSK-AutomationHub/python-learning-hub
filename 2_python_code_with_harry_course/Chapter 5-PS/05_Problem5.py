# Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

# s = {8, 7, 12, "Harry", [1,2]} 
# set can not have list inside it as set elements must be hashable, 
# list objects are mutable and therefore not hashable. 

s1 = {8, 7, 12, "Harry", (1,2)}

for item in s1:
    if type(item) == tuple:
        l = list(item)
        l.append(3)
        t= tuple(l)
        s1.add(t)
        s1.remove(item)        
        break
    
print(s1)

