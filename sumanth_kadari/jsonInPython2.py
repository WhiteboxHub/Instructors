import json

employee_dict = {"id":"09","name":"sumanth","dep":"ML"}
print("this is python",type(employee_dict))

#converting python to json
print("\nNow converting from python to json obj")

json_obj=json.dumps(employee_dict,indent=5)
print("converted to json",type(json_obj))
print(json_obj)