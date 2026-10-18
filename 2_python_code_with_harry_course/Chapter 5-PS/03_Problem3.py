my_set = {18, '18', 'test', True} # we can have a set with 18 (int) and '18' (str) as a value in it
print(my_set)

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print(len(s))
print(s)
# set takes unique values
# here 20 & 20.0 are treated as same value ingoring their data types (int, float)