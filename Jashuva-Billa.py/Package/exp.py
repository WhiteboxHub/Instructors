def greet():
    print("Hello from module1")


class Jashuva():                                                          
 def __init__(self,name,age,gender):                               
   self.name = name
   self.age=age
   self.gender=gender

 def work(self,profession):                                                       
     print(f"{self.name} age {self.age}, {self.gender} works on :",profession)
 
 def drives(self,Vechile):
     print(f"{self.name} drives {Vechile} to work")

 
Jashuva_details=Jashuva("Jashu",20,"Male")                                           
Jashuva_details.work("Python")                                                
Jashuva_details.drives("Vento")

