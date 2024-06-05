from dataclasses import dataclass, field

@dataclass
class Innovapath():
    """A class for holding an Innovapath company details"""
 
 
    Emp_name: str
    Emp_id: int
    Team: str
    language: str
    Designation:str= field (default= " Software developer")
 

# A DataClass object
Emp1 = Innovapath("Yatish","2010", " ML"," Python",)
Emp2 = Innovapath("Jashuva Billa","2011", " ML"," Python")
Emp3 = Innovapath("Sumanth ","2012", " ML"," Python")
Emp4 = Innovapath("Ajay ","2013", " ML"," Python")
Emp5 = Innovapath("Sai Teja ","2014", " DS"," Python")
print(Emp1)









@dataclass(order=True)
class people():
    "People of Hyderabad"

    sort:int= field(init=False,)

    Name:str
    age:int 
    gender:str
    pho:int=field(repr=False,compare=True)
    location:str= field (default="hyderabad",)
    
    def __post_init__(self):
        self.sort=self.age

P1=people("Jashuva",51,"Male",123456789)
P2=people("Devi",50,"female",2345678 )
P3=people("Jashuva",21,"Male",23454548)


print(P1)
print(P3)   
print(hash(P1.Name))
print(hash(P3.Name))
print(P1==P3)
print(P1<P2)














