class stud:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
        
        
    def stud_info(self):
        print("name :",self.name,"rollno:",self.rollno)
        lap1.lappy_info()
        
    class laptop:
        
        def __init__(self):
            self.brand = 'hp'
            self.model = 'i5'
        def lappy_info(self):
            print(self.brand,self.model)
        
        
obj1=stud("saleem",43)
obj2=stud("junaid",505)
lap1=stud.laptop()
print(obj2.stud_info())


