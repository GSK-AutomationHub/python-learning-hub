
def check_char_counts_1(text):
    freq = {}
    for char in text:
        freq[char] = text.count(char)
    return freq

from collections import Counter

def check_char_counts_2(text):
    freq = Counter(text)
    return dict(freq)


print(check_char_counts_1('racecar'))
print(check_char_counts_2('racecar'))