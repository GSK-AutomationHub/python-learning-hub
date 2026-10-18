countries = ('India', 'Russia', 'Israil', 'France', 'UAE')

india_info = {
    'priminister':'Narendra Modi',
    'Year': 2025,
    'Military Operation': 'Operation Sindoor'
}

print("-------------- Lambda Approach ------------------")
for country in countries:
    #print(country)
    (lambda x: print(x))(country)

print("-------------- Map Approach ------------------")
list(map((lambda x:print(x)),countries))


print("-------------- Dynamic function usage ------------------")
args = countries
kwargs = india_info

def dynamic_function(*args,**kwargs):
    return {'positional':args, 'keyword':kwargs}

result = dynamic_function(*args,**kwargs)
print(result)
list(map(lambda x:print(x),result.get('positional')))
for key,value in result.get('keyword').items():
    print(f"{key}:{value}")

print("-------------- is_prime usage ------------------")

num = range(1,30)
def is_prime(num):
    for x in range (num):
        if (num%2) == 0:
            return True
        else:
            return False

primes = list(filter(is_prime,num))
print(primes)