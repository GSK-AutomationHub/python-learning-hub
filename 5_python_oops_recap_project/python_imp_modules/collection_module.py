import collections
from collections import Counter
from collections import defaultdict
from collections import namedtuple

print(" ------------------------------- Counter --------------------------------------- ")

numbers = [1,1,1,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,9,9,9,9,9,9]
c = Counter(numbers)
print(c)
print(c.most_common(3))

str = "aaaaccccbbbbbdddddggggggggg"
s = Counter(str)
print(s)

sentence = "tell how many times the word appears in sentence having multiple word"
l = Counter(sentence.split())
print(l)

print(Counter("agobaithagobai"))

print(" ------------------------------- default-dict --------------------------------------- ")

dict = {'how': 1, 'many': 1, 'times': 1, 'sentence': 1}
try:
    print(dict)
    print(dict['how'])
    print(dict['word'])
except KeyError:
    print("Invalid Key")

new_dict = defaultdict(lambda: 1)
print(new_dict['word'])
print(new_dict)

print(" ------------------------------- named-tuple --------------------------------------- ")

Dog = namedtuple('Dog',['name','age','breed'])

doggy = Dog('sammy',5,'lab')
print(doggy)
print(doggy.name, doggy.breed)