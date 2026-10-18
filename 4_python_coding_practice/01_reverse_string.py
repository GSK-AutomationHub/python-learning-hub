
def reverse_string_1(text):
    return text[::-1]


def reverse_string_2(text):
    return "".join(reversed(text))


def reverse_string_3(text):
    reverse = ""
    for i in range(len(text)):
        reverse = text[i] + reverse
    return reverse


print(reverse_string_1("racecar"))
print(reverse_string_2("hello"))
print(reverse_string_3("hello"))