#classes and Objects

class JB:                                                          #created a class with name JB using class keyword
 def __init__(self,name,age,gender):                               # used pre defined INIT() method to initialise the objects
   self.name = name
   self.age=age
   self.gender=gender

 def work(self,language):                                                       #Methods() (Behaviour1)
     print(f"{self.name} age {self.age}, {self.gender} works on :",language)
 
 def drives(self,Vechile):
     print(f"{self.name} drives {Vechile} to work")

 def hobbie(self,Music):                                                         #Method() (behaviour2)
     print(f"{self.name} plays",Music)

 def prof(self,software):
   print(f"{self.name} works on ", software)

My_details=JB("Jashu",20,"Male")                                         #creating a instance of class        
My_details.work("Python")                                                #calling the method work 
My_details.drives("Vento")
My_details.hobbie("Guitar")
My_details.prof("vscode")



My_details=JB("Kiran kumar",25,"Male")
My_details.work("JAVA")
My_details.drives("polo")
My_details.hobbie("Drum kit")





























