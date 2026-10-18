
# iterable : 
    # anything than can be iterate through using for loop 
    # e.g collections like list, tuple, set

# iterator : 
    # Object of type iter, it uses dunder method __inter__ 
    # They keep track of their state using dunder method __next__ 
    # memory efficient and exhaustive 

# generator : 
    # powerful tool create iterator
    # type of lazy iterator uses yield keyword
    # returns one item at a time from sequence on demand using yield keyword
    # memory efficient and exhaustive 

from typing import Iterable, Iterator, Generator

peoples: list[str] = ['Vishal', 'Shashi', 'Anand'] # iterable

people_iter: Iterator[str] = iter(peoples) # iterator

# print(next(people_iter))
# print(next(people_iter))
# print(next(people_iter))
# print(list(people_iter))  # memory efficient and exhaustive 

def say_hello(names:Iterable[str]):
    for name in names:
       yield f"Hello {name}, Warm Welcome!"

def greet_person(func):
    yield from func

greetings = greet_person(say_hello(peoples))
print(next(greetings))
print(next(greetings))
