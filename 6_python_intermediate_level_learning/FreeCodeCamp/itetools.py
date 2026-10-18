from itertools import product, permutations, combinations, combinations_with_replacement
from itertools import accumulate ,groupby, count, cycle, repeat

# product
a = [1,2]
b = [3,4]
prod = product(a,b)
print("product result: ", list(prod))


# permutations
c = [1,2,3]
perm = permutations(c)
print("permutations result: ",list(perm))


# combinations
d = [1,2,3]
comb = combinations(d, 2)
print("combinations result: ",list(comb))
comb_wr = combinations_with_replacement(d,2)
print("combinations with replacement result: ",list(comb_wr))


# accumulate
# e = [1,2,3,4]
# acc = accumulate(a, func=lambda x: x+2)
# print("accumulation result: ",list(e))


# groupby
person = [{'name':'Tim', 'age': 42}, 
          {'name':'gorge', 'age': 51}, 
          {'name':'ellena', 'age': 32},
          {'name':'Ivan', 'age': 42},
          {'name':'Max', 'age': 51},
          {'name':'steve', 'age': 32}
          ]
person_sorted = sorted(person, key=lambda x: x['age'])
person_group = groupby(person_sorted, key=lambda x:x['age'])
for key, value in person_group:
    print(key, list(value))


# count
for i in count(1):
    print(f"5 * {i} = {5*i}")
    if i == 10:
        break


# cycle
cnt = 1
a = [1,2,3]
for i in cycle(a):
    print(a)
    cnt+=1
    if cnt == 4:
        break


# repeat
cnt = 1
for i in repeat(cnt):
    print("I am confident")
    cnt+=1
    if cnt == 4:
        break


def test_iter_function():
    s = [1,2,3,4,5,6,7,8,9]

    itr = iter(s)

    try:
        for i in range(12):
            print(next(itr))
    except StopIteration as e:
        print("Exception got Handeled", e)
    else:
        print("Execution without error")
    finally:
        print("Execution Completed")
