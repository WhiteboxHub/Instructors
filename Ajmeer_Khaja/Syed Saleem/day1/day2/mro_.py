class A:
    def __init__(self  ) -> None:
        print("from a init")
    
    def func1(self):
        print("feature of funtion 1")
        
    def func2(self):
        print("feature of funtion 2")
        
class B:
    def __init__(self, name) -> None:
        print("from b init")
    
    
    def func3(self):
        print("feature of funtion 3")
        
    def func4(self):
        print("feature of funtion 4")
        
class C(A,B):
    def __init__(self) -> None:
        print("from c init")
        super().__init__()
    
    
    def func3(self):
        print("feature of funtion 3")
        
    def func4(self):
        print("feature of funtion 4")
        

        
a1=C()



