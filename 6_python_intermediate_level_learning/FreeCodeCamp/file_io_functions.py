import os

def write_to_file(filename, content):
    with open(filename, "x") as f:
        f.write(content)
        print(f"####### Successfully created the New file '{filename}' #######")

def read_the_file(filename):
    with open(filename, "r") as f:
        data = f.read()
        print(data)
        return data

def check_for_word(filename, word):
     with open(filename, "r") as f:
        data = True
        line_no = 1
        while data:
            data = f.readline()
            if(word in data):
                print(f"word '{word}' found in file at line number '{line_no}'")
                return
            line_no +=1
        print(f"word '{word}' not found in file")
        return -1

def replace_the_word(filename, old_word, new_word):
    if check_for_word(filename, old_word)!= -1:
        with open(filename, "r") as f:
            data = f.read()
            new_data = data.replace(old_word, new_word)
        with open(filename,"w") as f:
            f.write(new_data)
    else:
        print(f'The word \'{old_word}\' not found in file')


def teardown(filename):
    os.remove(filename)
    print(f"####### Successfully removed the file '{filename}' #######")