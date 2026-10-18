import csv

string_list = [["column1", "column2", "column3"], 
               ["R1C1", "R1C2", "R1C3"],
               ["R2C1", "R1C2", "R1C3"]]

file_path = ".\\csv_file.csv"

def gen_content(data):
    for row in data:
        yield row


def write_to_csv(content):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(content)


def read_from_csv():
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            yield row


write_content = gen_content(string_list)
write_to_csv(next(write_content))
write_to_csv(next(write_content))


read_content = read_from_csv()
print(next(read_content))
print(next(read_content))
