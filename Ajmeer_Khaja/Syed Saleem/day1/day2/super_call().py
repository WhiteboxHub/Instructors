class A:
    def __init__(self  ) -> None:
        print("from a init")
    
    def func1(self):
        print("feature of funtion 1")
        
    def func2(self):
        print("feature of funtion 2")
        
class B(A):
    def __init__(self, name) -> None:
        super().__init__()
        self.name=name
        print(name)
    
    
    def func3(self):
        print("feature of funtion 3")
        
    def func4(self):
        print("feature of funtion 4")
        
a1=B("akbar")



