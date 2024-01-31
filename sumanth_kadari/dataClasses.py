from dataclasses import dataclass
@dataclass
class Person:
    name:str
    age:int
    profession:str


person1=Person("Sumanth",22,"ML")  #creating class instance
print(person1)


person1.profession="Full stack dev"  #we can override atrr values here using atrr name
print(person1)

#IMMUTABLE CLASS   
'''@dataclass (frozen=True) #using frozen we can't change the attr value once we assigned
class point:
    x:int()
    y:int()
point1=point(2,4)
print(point1)

point1.x=5'''  #here overrie the attr value

#inheritance
@dataclass
class person:
    name:str
    age:int

@dataclass
class Employee(person):
    employee_id=str
    department=str

person2=person("sumanth",22)

employee=Employee('sumanth',22,) #here i'm inheritating parent to child class
print(employee)


#nested DataClasses

@dataclass
class Address:
    street:str
    city:str
    zip_code:str

@dataclass
class menPerson:
    name:str
    age:int
    address:Address

address=Address("123 street","Hyd","501301")
men=menPerson("sumanth",22,address)
print(men)






