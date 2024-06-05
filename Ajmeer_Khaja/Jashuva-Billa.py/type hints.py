#lets check out the Type Hints 
"""
from typing import List,Tuple,Union"""

def Type(Name:str,age:int) :
 
 print("Name = ",Name, "\nAge =",age)

Type(23,22) 



def userdata()->None : 
 data:str= input(" Please enter yor name")
 Teammates:list=input(" please enter the Team members name")
 Team_details:dict=input(" enter the team details")
 print(data)
 print(Teammates)
 print(Team_details)

userdata()
