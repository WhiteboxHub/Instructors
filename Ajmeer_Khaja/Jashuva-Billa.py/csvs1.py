import csv

data = [
    ['Name', 'Age', 'Country'],
    ['Alice', 30, 'USA'],
    ['Bob', 25, 'UK'],
    ['Charlie', 35, 'Canada']
]

csv_file = 'data.csv'


with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print(f"CSV file '{csv_file}' has been created successfully!")

with open(csv_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)