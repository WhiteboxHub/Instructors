class MyMeta(type):
    pass
class MyClass(metaclass=MyMeta):
    pass
class MysubClass(MyClass):
    pass
print(type(MyMeta))   #wht type data there in the above classes
print(type(MyClass))
print(type(MysubClass))


class UppercaseMeta(type):
    def __new__(cls, name, bases, dct):
     
        for attr_name, attr_value in dct.items():     # Iterate through class attributes
            if isinstance(attr_value, str) and attr_value.islower():
                # If the attribute is a lowercase letter, replace it with its uppercase equivalent
                dct[attr_name] = attr_value.upper()
        # Call the __new__ method of the superclass (type) to create the class
        return super(UppercaseMeta, cls).__new__(cls, name, bases, dct)

class LowercaseLetters(metaclass=UppercaseMeta):
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    
lowercase_instance = LowercaseLetters()   # Instantiate the class

print(lowercase_instance.a)         #Print the modified attributes
print(lowercase_instance.b) 
print(lowercase_instance.c)  
print(lowercase_instance.d) 



        