# Write a recursive function to calculate the sum of first n natural numbers

def get_recursive_sum(n):
    if type(n) != int:
        print("Please enter valid positive integer")
    elif n < 0:
        print("Please enter valid positive integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + get_recursive_sum(n-1)
    

print(get_recursive_sum(5))