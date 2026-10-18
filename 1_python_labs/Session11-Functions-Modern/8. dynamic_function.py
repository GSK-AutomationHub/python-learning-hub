
def dynamic_function(*args, **kwargs):
    return {'positional':args, 'keyword': kwargs}

args = ["orange", "red", "white", "blue", "green"]
kwargs = {
    "name":"Amit",
    "role": "Automation Lead",
    "salary": 6000000
}

result = dynamic_function(*args,**kwargs)
print(type(result), result)

colors = result.get('positional')
print(type(colors), colors)
for color in colors:
    print(color)

employe_details = result.get('keyword')
print(employe_details.get('name'), employe_details['role'], employe_details['salary'])
for i, v in employe_details.items():
    print(f"{i}: {v}")