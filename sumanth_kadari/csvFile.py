import csv

data=[
    ["name","age","location"],
    ["sumanth",22,"Hyd"],
    ["bunny",23,"wgl"]
]

file_name= "data.csv"

with open(file_name,"w",newline="")as csvfile:
    writer =csv.writer(csvfile)
    
    for row in data:
        writer.writerow(row)
print(f"csv file {file_name} has been created succesfully" )