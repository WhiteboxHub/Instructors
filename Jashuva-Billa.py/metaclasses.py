Office=type("Innovapath",(),{"Start_date":"1 Feb 2024", "Role" :" ML"} )

print(Office.Start_date)



















class Meta(type):
    def __new__(cls, name, bases, dct):
        print("Creating class:", name)
        print("Bases:", bases)
        print("Attributes:", dct)
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    attr = 42
    

    def method(self):
        return "Hello, world!"

obj = MyClass()
print(obj.method())