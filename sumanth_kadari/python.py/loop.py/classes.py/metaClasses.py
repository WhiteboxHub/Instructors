class MyMeta(type):
    pass
class MyClass(metaclass=MyMeta):
    pass
class MySubClass(MyClass): 
    pass
print(type(MyMeta))
print(type(MyClass))
print(type(MySubClass))