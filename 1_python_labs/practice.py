
x = 25

class TestSample:
    x = 15

    def sample(self):
        x = 12
        print(f"global var x = {globals()['x']}, class var x = {self.x}, local var x = {x}")

obj = TestSample()
obj.sample()

y = {
    'name': 'abhay',
    'marks': 95,
    'price': 250.25,
    'is_good_to_buy':True,
    'item_list': [1,2,3,4,5,6]
}

print(y)
print(y['item_list'][3])

str = "Let’s see how to double each elements of the given list"
str_to_list = str.split()
print(type(str_to_list), str_to_list)

back_to_str = ' '.join(str_to_list)
print(type(back_to_str), back_to_str)

str_with_delimiter = str.replace(' ', '-')
print(type(str_with_delimiter), str_with_delimiter)

list1 = [3,5,7,9,12]
list2 = ['blue','red','green']
combo_list = list1 + list2
print(combo_list)
list1.extend(list2)
print(list1)
list3 = list()
print(len(list3))

list4 = [3,12,5,15,7,27,9,32]
list4.sort()
print(list4)
list5 = [3,12,5,15,7,25,27,9,32,30]
print(sorted(list5))

list4.sort(reverse=True)
print(list4)
print(sorted(list5,reverse=True))

list6 = []
assert bool(list6), "list is empty"