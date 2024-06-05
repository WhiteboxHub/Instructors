class A:
    
    def __init__(self,name) -> None:
        self.name=name
        print(name)
    
    def func1(self):
        print("feature of funtion 1")
        
    def func2(self):
        print("feature of funtion 2")
        
class B(A):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.name=name
    
    
    def func3(self):
        print("feature of funtion 3")
        
    def func4(self):
        print("feature of funtion 4")
        
a1=B("pandu")
a1.name="ajmal"


print(a1.name)