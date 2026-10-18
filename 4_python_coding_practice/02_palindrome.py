
def is_palindrome_1(text):
    if text == text[::-1]:
        print(f"{text} is palindrome")
    else:
        print(f"{text} is not palindrome")


def is_palindrome_2(text):
    if text == "".join(reversed(text)):
        print(f"{text} is palindrome")
    else:
        print(f"{text} is not palindrome")

is_palindrome_1("madam")
is_palindrome_2("hello")