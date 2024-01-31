import json
with open("states.json",'r') as f:  # here iam using open keyword to read the json file
    data = json.load(f)            #by giving json.load, it will load the data
for k in data['states']:           # by using for loop we will print all the staff
    del k['area codes']             # here iam deleting area codes
                      
with open('new states.json','w') as f:  # in this statements, after deleting the area codes,iam creating a new file to stores the data
    json.dump(data,f , indent=2)         # by using indent, the quality of data improved