# even number till 50

even_numbers = [ number for number in range(0,51) if number % 2 == 0]

print(even_numbers, len(even_numbers))

for number in even_numbers:
    print(number, end=' ')


even_numbers_with_generator = (number for number in range(0,51) if number % 2 == 0)
print("\n")
print(next(even_numbers_with_generator))
print(next(even_numbers_with_generator))
print(next(even_numbers_with_generator))
print(next(even_numbers_with_generator))
print(next(even_numbers_with_generator))

