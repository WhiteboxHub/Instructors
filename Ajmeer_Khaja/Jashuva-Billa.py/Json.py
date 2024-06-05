"""import json


json_data = '''
{

    "name": "Jashu",
    "age": 30,
    "city": "Hyderabad",
    "is_student": false,
    "grades": [95, 87, 91]

}
  
'''


data_dict = json.loads(json_data)

print("Dictionary from JSON data:")
print(data_dict)
print()


print("Accessing individual fields:")
print("Name:", data_dict['name'])
print("Age:", data_dict['age'])
print("City:", data_dict['city'])
print("Is Student:", data_dict['is_student'])
print("Grades:", data_dict['grades'])
print()

data_dict['age'] = 35
data_dict['grades'].append(88)


modified_json_data = json.dumps(data_dict, indent=4)


print("Modified JSON data:")
print(modified_json_data)



"""




import json


json_data = '''
[
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35}
]
'''

data = json.loads(json_data)

sorted_data = sorted(data, key=lambda x: x['name'])
sorted_json_data = json.dumps(sorted_data, indent=4)


print(sorted_json_data)



