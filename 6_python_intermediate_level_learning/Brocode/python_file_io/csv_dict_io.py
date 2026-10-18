import csv

crick_match_list = [{'team':'ind vs pak', 'date': '12-12-2022'},
    {'team':'ind vs aus', 'date': '12-16-2022'},
    {'team':'ind vs eng', 'date': '12-24-2022'}
]

file_path = ".\\python_file_io\\csv_dict_file.csv"

def gen_content(data):
    for row in data:
        yield row


def write_dict_file(content, is_header_written = None):
    fieldnames = list(crick_match_list[0].keys())
    with open(file_path,'a', newline='') as file:
        dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
        if is_header_written == False:
            dict_writer.writeheader()
            dict_writer.writerow(content)
        else:
            dict_writer.writerow(content)


def read_dict_file():
    with open(file_path,'r', newline='') as file:
        dict_reader = csv.DictReader(file)
        for row in dict_reader:
            yield row


write_content = gen_content(crick_match_list)

try:
    write_dict_file(next(write_content), False)
    write_dict_file(next(write_content), True)

except Exception as e:
    print(e)
else:
    print("all record got printed wo error")
finally:
    print("dict file writing completed")

read_content = read_dict_file()
print(next(read_content))
print(next(read_content))