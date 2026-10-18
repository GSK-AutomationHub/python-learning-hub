name, age, salary = 'Vijay', 30, 500000

# Approach 1 - with , delimiter
print('Name is: ', name)  # java uses + but python uses , as seperator
print('Age is: ', age)
print('Salary is: ', salary)

# Approach 2  - with %s,%d,%g %(args)
print('Name is: %s, Age is: %d Salary is: %g' %(name, age, salary))

# Approach 3 - with {} .format(args)
print('Name is: {}, Age is: {} Salary is: {}'.format(name, age, salary))
print('{} of age {} have salary {}'.format(name, age, salary))

# Approach 4 - with f string - f 'some data with {placeholder}'
print(f'{name} of age {age} have salary {salary}')