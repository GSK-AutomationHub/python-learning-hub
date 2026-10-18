from file_io_functions import write_to_file, read_the_file

content = '2, 5, 7, 8, 10, 12, 17, 21, 34'
filename = "temp.txt"

# write_to_file(filename,content)
data = read_the_file(filename)
print(data, type(data))
str_data_list = data.split(",")
int_data_list = []
for i in range(len(str_data_list)):
    str_data_list.insert(i,int(str_data_list.pop(i)))
print(str_data_list)
count = 0
for i in str_data_list:
    if (i % 2 == 0):
        print(f"list has even number {i}")
        count+=1
print(f"list has total {count} even numbers")