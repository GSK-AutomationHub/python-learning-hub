# There are two types of function arguments in python - positional, keyword

def func(i, j, args='positional'):
    print(i, j, args)


func(10, 20, 'positional')  # position argument

func(10, 20,)  # valid position argument
# Note - here default value of args positional argument will be considered as no param specified

func(i=10, j=20, args='keyword')  # keyword argument

func(args='keyword', j=20, i=10)  # valid keyword argument,
# Note - order of arguments doesn't matter in case of keyword argument

func(10, j=30, args = 'positional + keyword')  # valid combination of position - keyword arguments

try:
    #func(j=30, 10, args = 'positional + keyword')  # Invalid combination of position - keyword arguments
    print("func(j=30, 10, args = 'positional + keyword')")
    print("# Invalid combination of position - keyword arguments")
    print('Note - positional argument must appears before keyword argument')
    print("func(10, i=20, args='positional + keyword')")
    func(10, i=20, args='positional + keyword')  # Invalid combination of position - keyword arguments
except Exception as e:
    print('# error message for invalid argument syntax - ', e)

