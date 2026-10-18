
from collections import Counter
import json

filepath = ".\\python_file_io\\Lion_King.txt"
word_list = list()

with open(filepath,'r') as f:
    lines = f.readlines()
    for line in lines:
        word_list.extend(line.split())

    total_word_count = len(word_list)
    print(f"The total word count in file content is {total_word_count}")

    unique_word_list = list(set(word_list))
    unique_word_count = len(unique_word_list)
    print(f"The unique word count is {unique_word_count}")

    word_count_dict = dict(Counter(word_list))
    # print(f"The words with their count are {json.dumps(word_count_dict, indent=4)}")

    repeating_words = dict(filter(lambda x :x[1] > 1, word_count_dict.items()))
    print(f"The repeated words with their count are \n{json.dumps(repeating_words, indent=4)}")

    repeating_words_sorted_by_count = dict(sorted(repeating_words.items(), key=lambda x: x[1], reverse=False))
    print(f"The repeated words info sorted format is \n{json.dumps(repeating_words_sorted_by_count, indent=4)}")

    most_repeated_word = repeating_words_sorted_by_count.popitem()
    print(f"The most repeated words in file is '{most_repeated_word[0]}', it appeared '{most_repeated_word[1]}' times ")