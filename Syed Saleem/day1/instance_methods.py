class student:
    """sakjjfodsvfjsnvdfjnvdfopszhasogheowgh"""
    

    
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
        
    def get_m1(self):
        return self.m1
        
    def get_m2(self):
        return self.m2
    def get_m3(self):
        return self.m3  
    
    def set_m1(self,value):
         self.m1=value
        
        
        
      
s1=student(43,23,33)
s2=student(43,65,76)
s2.m1=65
s1.set_m1(90)
sgm=s1.get_m1()
gm=s2.get_m1()
print(sgm)
print(s2.avg())


print(dir(s1))
print(s1.__doc__)