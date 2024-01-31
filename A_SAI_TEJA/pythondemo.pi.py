import csv  
  
data = [    ['Name', 'Age', 'Country'],  
    ['Alice', '25', 'USA'],  
    ['Bob', '30', 'Canada'],  
    ['Charlie', '35', 'Australia']  
]  
  
with open('data.csv', 'w') as file:  
    writer = csv.writer(file)  
    for row in data:  
        writer.writerow(row)  
