import csv, json

with open(".\\python_file_io\\actor_movie.csv", 'r', newline='') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]


with open(".\\python_file_io\\actor_movie.json", 'x+', newline='') as json_file:
    json.dump(rows, json_file, indent = 4)


