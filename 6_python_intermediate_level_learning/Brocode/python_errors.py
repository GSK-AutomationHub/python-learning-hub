
print("-------------------------- Import / ModuleNotFound Error ----------------------------------")
# Import error & ModuleNotFound error : occurs when we try to import module not exist
try:
    from math import bob
except ImportError as e:
     print(e)

try:
    import bob
except ModuleNotFoundError as e:
    print(e)


print("-------------------------- Attribute Error ----------------------------------")
# Attribute error : occurs with . operator e.g. access attribute / methods not exits in class or private
class Sample:
    __sample_var = 30

s1 = Sample()
try:
    #print(s1.name , s1.play_music()) # it ll give attribute error
    print(s1.sample_var) # it ll give attribute error as attribute is private
except AttributeError as e:
    print(e)


print("-------------------------- Name Error ----------------------------------")
# Name error: occurs when try to access / print something which do not exist / not defined / deleted
try:
    print(high_score) 
except NameError as e:
    print(e)



print("-------------------------- Key Error ----------------------------------")
# Key error: occurs when try to access dict value with key whch does not exist
employee_record = {
    'name':'Ashish',
    'ID': 'ABC123',
    'Salary': '42 LPA',
    'Role': 'Lead Consultant'
}

try:
    print(employee_record['company'])
except KeyError as e:
    print(e)


print("-------------------------- Type Error ----------------------------------")
# Type error: occurs at multiple places e.g.
    # If default param 'self' is missed for class method n method being called using object 
    # If try to create object of abstract class
    # If tries to update the tuple item [tuple is immutable]
    # If tries to print set item with particular index 

# If default param 'self' is missed for class method n method being called using object 
class A:
    def sample_method(): # -->  self is missing
        print('this is sample method of class A') 

obj = A()
try:
    obj.sample_method() #--> Type Error
except TypeError as e:
    print(e)

# If try to create object of abstract class
from abc import ABC, abstractmethod

class B(ABC):
    @abstractmethod
    def sample_one(self):
        pass 
try:
    obj = B() #--> Type Error
except TypeError as e:
    print(e)

# If tries to update the tuple item [tuple is immutable]
a = (1, 3 ,5, 7, 9)
try:
    a[3] = 15 #--> Type Error
except TypeError as e:
    print(e)

# If tries to print set item with particular index 
a ={1, 3 ,5, 7, 9}
try:
    print(a[3]) # --> Type Error
except TypeError as e:
    print(e)


print("-------------------------- Value Error ----------------------------------")
# value error : occurs when incorrect type casting like string to int
try:
    print(int('ten'))
except ValueError as e:
    print(e)



print("-------------------------- Index Error ----------------------------------")
# Index error : occurs index is out of range
numbers = [1,2,3,4,5]
try:
    print(numbers[6])
except IndexError as e:
    print(e)


print("-------------------------- StopIteration Error ----------------------------------")
# Index error : occurs index is out of range
numbers = [1,2,3]

def gen_num_itr(Iterable:int):
    for itr in Iterable:
        yield itr

num_itr = gen_num_itr(numbers)
for i in range (len(numbers) + 1):
    try:
        print(next(num_itr))
    except Exception as e:
        print(f"An '{type(e).__name__}' error occurred") 


print("-------------------------- NotImplemented Error -------------------------")

# class TestClass:
#     raise NotImplementedError("Pending Implementation")

def sample_method():
    raise NotImplementedError("Pending Implementation")

try:
    sample_method()
except NotImplementedError as e:
    print(e)


print("-------------------------- Syntax Error -------------------------")
# try:
#     print("Hello World) # ---> unterminated string literal
# except SyntaxError as e:
#     print(e)


print("-------------------------- Indentation Error -------------------------")

# def test_func():
# print(2 + 3)  # ---> expected an indented block after function definition