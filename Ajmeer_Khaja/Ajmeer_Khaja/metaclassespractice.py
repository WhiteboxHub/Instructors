# class check:
#     print("The check class is created")
#     # print(f"{type(check)=}")
#     def __init__(self,name,age):
#         self.name=name
#         self.age = age
#     def __str__(self):
#         return f"{self.name} age is {self.age}"
#     def checkprint(cls,*args,**kwargs):
#         print(f"The args are {args=},{kwargs=}")
#         return 3
#     def checkfun(self):
#         print("This is a check check function")


# c1 = check('ajmeer',33)
# print(c1)
# c1.checkfun()
# c1.checkprint(3,5)


class NoisyMeta(type):
    @classmethod
    def __prepare__(meta,name,bases):
        print("Entering __prepare__")
        print(f"print >> {name} and {bases}")
        print(f"{meta=}")
        namespace = super().__prepare__(name,bases)
        return namespace
    @staticmethod
    def __new__(meta,name,bases,attrs):
        print("Entering __new__")
        print(f"{name} and {bases}")
        print(f"{attrs=}")
        result = super().__new__(meta,name,bases,attrs)
        return result
    
    def __init__(cls,name,bases,attrs):
        print("Entering __init++")
        print(f"printing {cls} and{name,bases}with {attrs=}")
        result = super().__init__(name,bases,attrs)
        return result
    def __call__(cls,*args,**kwargs):
        print("Entering __call__")
        print(f"{cls=} and {args=}")
        result = super().__call__(*args,**kwargs)
        return result