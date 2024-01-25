import csv

students = [{'No': 1, 'name': 'Anu', 'role': 'student'},
            {'No': 2, 'name': 'john', 'role': 'student'},
            {'No': 3, 'name': 'Manu', 'role': 'student'}]

csv_file_path = 'name.csv'

with open(csv_file_path, 'w', newline='') as csv_f:
    field_names = list(students[0].keys())
    csv_writer = csv.DictWriter(csv_f, fieldnames=field_names)
    csv_writer.writeheader()
    csv_writer.writerows(students)
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv_file.readlines()

for line in csv_reader:
    print(line, end="")
