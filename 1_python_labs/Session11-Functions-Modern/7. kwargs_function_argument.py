"""
• *kwargs can be used as dynamic function parameter to pass any no of keyword arguments to the function

• Similarly if any function takes multiple arguments then that can be passed to function using *args using list

• Function using *kwargs if have return statement, then returns type is always Dictonary

"""

def sample_one(**kwargs):
    print(type(kwargs))
    for i,v in kwargs.items():
        print(f"{i} : {v}")

sample_one(name="Amit", role="Automation Lead", salary=6000000)


print("---------------------------------------------------------------")

def sample_two(name, role, salary):
    print(type(kwargs))
    for i,v in kwargs.items():
        print(f"{i} : {v}")

kwargs = {
    "name":"Amit",
    "role": "Automation Lead",
    "salary": 6000000
}
sample_one(**kwargs)