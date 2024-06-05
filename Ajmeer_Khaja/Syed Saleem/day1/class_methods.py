class student:
    
    
    class_variable=10
    
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    @classmethod  
    def modify_class_var(cls,new_value):
        cls.class_variable = new_value
        
        
s1=student(23,43,76)
student.modify_class_var(20)
print(student.class_variable)
print(s1.__dict__)