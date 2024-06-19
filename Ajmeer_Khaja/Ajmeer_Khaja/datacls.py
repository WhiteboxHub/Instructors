from dataclasses import dataclass,field
from typing import List
import time
from datetime import datetime
# @dataclass
# class Point:
#     x:int
#     y:int
  
#     # print(name,age,exp)

#     def multipy(self) -> float:
#         return self.x*self.y
    

#     def __init__(self,name:str,age:int,exp:int):
#         self.name =name
#         self.age =age
#         self.exp = exp

#     def __str__(self):
#         return f"The name is {self.name} with exp of {self.exp} at age {self.age}"

# p1 = Point(1,2,"ajmeer")
# p2 = Point(1,2,"ajmeer")


# print(p2)
# print(p1)
# print(p1==p2)


# @dataclass

# class newcls:
#     name:str
#     age:int
#     location:str

# n1 = newcls('ajmeer',22,'hyd')

# n2 = newcls('khaja',44,'pbr')
# # print(n1)
# # print(n2)



# @dataclass

# class personal_info:
#     username:str
#     verification:bool
#     name:str
#     age:int
#     loginSection : List[datetime] = field(default_factory=list)
#     logoutSection: List[datetime] = field(default_factory=list)

#     def add_login_session(self):
#         timenow = datetime.now()
#         if(self.verification):
#             self.loginSection.append(timenow)
#         else:
#             print('Verify Account to login')
    

#     def add_Logout_session(self):
#         ##string the previous login section
#         if(len(self.loginSection)>0):
#             prevLoginSession = self.loginSection[-1]
            
#             timenow = datetime.now()

#             if(prevLoginSession<timenow):
#                 self.logoutSection.append(timenow)
#             else:
#                 print(self.name," has not logged in ")
    

# user1 = personal_info('aka2001',True,"ajmeer",22)

# for i in range(5):
#     user1.add_login_session()
#     time.sleep(1)
#     user1.add_Logout_session()
# print(user1)



@dataclass
class StudentInfo:
    
    sname:str
    sclass:int
    sage:int

@dataclass
class attendence(StudentInfo):
    sattendence : List[str] = field(default_factory=list)
    def mark_attendence(self):
        nowtime = datetime.now()
        nowdate = nowtime.second
        nowmonth = nowtime.month
        today = f"{nowdate}-{nowmonth}"
    def check_attendence_qualification(self):
        percentage = len(self.sattendence)*100/20
        if(percentage<75):
            print(f"{self.name} has low attendence % of  {percentage}")
            # raise detained(f"{self.name} student is detained")
        else:
            print(f"{self.name} is eligible for examination")


# try:
#     s1 = StudentInfo('tom',3,9)
# except detained as e:
#     print(e)

s2 = attendence('leo',10,16)
 
for i in range(18):
    
    s2.mark_attendence()

s2.check_attendence_qualification()
    