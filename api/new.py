import csv

csv_file_path = 'C:/Users/Nazim/Desktop/djangoAPI/backend/static/Report Trial Task - Performance.csv'

def handle_numeric_value(value):
    if value.isdigit():
        return int(value)
    return 0

with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for key, value in row.items():
            if value in ('-', ''):
                value = 0
            print(value)

