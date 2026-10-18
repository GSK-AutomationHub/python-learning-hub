
person = [{'name':'Tim', 'age': 42}, {'name':'gorge', 'age': 51}, {'name':'ellena', 'age': 32}]

# sorted()
persons_by_age = sorted(person, key=lambda x: x['age'])
print(person)
print("person sorted by age: ", persons_by_age)

# filter
persons_above_40 = filter(lambda x: x['age']>50, person)
print("person with age above 50: ", list(persons_above_40))

# map
person_age_plus_10 = map(lambda x: x['age']+10, person)
print("person with age plus 10: ", list(person_age_plus_10))

person_name_plus_sen = map(lambda x: x['name']+' sen', person)
print("person name with sen suffix: ", list(person_name_plus_sen))

person_group_update = map(lambda x: (x.update({'group':'bike riders'}) or x), person)
print("person with group name update: ", list(person_group_update))

person_city_update = [ {**p,'city':'Boston'} for p in person]
print(person_city_update)