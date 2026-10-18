def division(x,y):
    return (x/y)

try:
    div = division(10,2)
    print(f"result of division is {div}")
except TypeError:
    print("received TypeError")
except ValueError:
    print("received ValueError")
except ZeroDivisionError:
    print("received ZeroDivisionError")
else:
    print("division calculated successfully")
finally:
    print("division task completed")