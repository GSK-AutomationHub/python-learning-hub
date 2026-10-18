

def demo_function(arg1, *args, **kwargs):
    print(type(arg1), arg1)
    print(type(args), args)
    print(type(kwargs), kwargs)
    return {arg1: arg1, 'positional':args, 'keyword':kwargs}

demo_result = demo_function(3, 30,60,90,name='alice', age=30,intrest = 'python programing')

dict = demo_result.get('keyword')
print(dict)
print(demo_result.get('keyword')['intrest'])