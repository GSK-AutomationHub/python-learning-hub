def gen_feb_series_till(n):
    if n == 0:
        print(f"fib series till given term is {n}")
    elif n == 1:
        print(f"fib series till given term is 0 , {n}")
    else:
        a , b = 0, 1
        temp = count = 0
        print(a, b, end=' ')
        while count <= n:
            temp = a + b
            yield temp
            a = b
            b = temp
            count +=1
            
fib_series_iterator = gen_feb_series_till(30)
for i in range(6):
    print(next(fib_series_iterator), end=' ')
