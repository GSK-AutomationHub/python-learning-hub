from file_io_functions import *

content = "Hi everyone\nI am learning file I/O\nusing Java\nI like programming in Java"
filename = "practice.txt"
word = "learning"
old_word = "Java"
new_word = "Python"

write_to_file(filename,content)

read_the_file(filename)

check_for_word(filename, word)

replace_the_word(filename,old_word,new_word)

read_the_file(filename)

teardown(filename)