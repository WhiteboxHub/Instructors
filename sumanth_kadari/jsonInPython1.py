import json  #convert from JSON to Python object

#here i'm taking json string
employee = '{"id":"09","name":"sumanth","dep":"ML"}'

print("this is a json",type(employee))


#converting json strng into python dic
employee_dict = json.loads(employee)
print("converted to python",type(employee_dict))
print(employee_dict)