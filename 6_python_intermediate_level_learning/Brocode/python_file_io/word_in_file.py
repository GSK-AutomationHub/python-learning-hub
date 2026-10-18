
filepath = ".\\python_file_io\\Lion_King.txt"
word = 'jjjjj'

def find_if_word_present_in_file(path_to_file, phrase):
    with open(path_to_file) as f:
        phrase_dict = {}
        count, lines = 0, list()
        content_list = f.readlines()
        for line in range (len(content_list)):
            if phrase in content_list[line]:
                lines.append(line)
                count+=1
                phrase_dict.update({'phrase': phrase, 'appears_at_lines' : lines, 'total_count' : count})
                print(f"the phrase '{phrase}' present in file at line number {line}")
                #break
            else:
                None

        if phrase_dict.get('phrase') == None:
            print(f"the phrase '{phrase}' not present in file")

        return phrase_dict

print(find_if_word_present_in_file(filepath, word))