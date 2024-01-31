'''
keys wont have duplication
but value has
'''

d={'a': 1,1:'abc','b':2}    #key value pairs
print(type(d))       #give the datatype name
print(d['a'])        #it will print the key value
print(d[1])          #it will print the key 
print(d.items())     #it will print all the keys and values
print(d.keys())      #it will give only keys
print(d.values())    #it will give only values
print(d.get('a'))    #by giving a key we will get value
print(d.pop(1))      #taking out a key from the dictionary
d.update({'c':123})  #it will add the given data in the dictionary
print(d)

for i,j in {'a': 1,1:'abc','b':2}.items():
    print(i,j)