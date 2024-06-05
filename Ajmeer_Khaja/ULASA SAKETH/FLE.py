#iam impoting Names.csv file

import csv
with open('Names.csv','r') as csv_file:
    csv_reader =csv.reader(csv_file)

    for s in csv_file:
        print(s)

