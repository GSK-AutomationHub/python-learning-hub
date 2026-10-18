from collections import Counter, defaultdict,deque

my_str = 'aaaaabbbcc'
my_counter = Counter(my_str)
print(type(my_counter))
print(my_counter)
print(dict(my_counter))
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(list(my_counter.elements()))

my_dict = defaultdict(int)
my_dict['a'] = 5
my_dict['b'] = 10
print(my_dict)
my_dict['c']
print(my_dict)

d = deque()

d.append(3)
d.append(6)
d.append(9)

print(d)
d.appendleft(2)
print(d)
d.extend([12,15])
print(d)
d.extendleft([0,1])
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.rotate(-2)
print(d)
print(list(d))