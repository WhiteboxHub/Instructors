# Single level inheritance                A->B   
class Phone:                              #creating a Parent class
    def __init__(self,name):
        self.name=name

    def fun(self):                                        #initialising a method()
            print(f"{self.name} I can call ")




class Mobile(Phone):                        #inheriting methods from parent class
    def __init__(self,name):
        self.name=name

    def work(self):
            print(f"{self.name} I can browse Internet")


"""
C1=Phone("landline")
C1.fun()"""

C2=Mobile("Smart phone")
C2.work()
C2.fun()


















#Multi level inheritance       A->B->C


class Phone:                              #creating a Parent class
    def __init__(self,name):
        self.name=name

    def fun(self):                                        #initialising a method()
            print(f"{self.name} I can call ")




class keypad(Phone):                                  #inheriting methods from Phone 
    def __init__(self,name):
        self.name=name

    def fea(self):
            print(f"{self.name} I am portable ")



class Mobile(keypad):                                   #inheriting methods and Keypad class
    def __init__(self,name):
        self.name=name

    def pro(self):
          print(f"{self.name} I can capture Images too ")
          
'''
C1=Phone("landline")
C1.fun()
'''
'''C2=keypad("Nokia")
C2.fea()
C2.fun()
'''

C3=Mobile("Smart phone")
C3.fun()
C3.fea()
C3.pro()
















#Multiple inheritance                    A->C ,B->C   = (A,B)-> C


class Phone:                              #creating a Parent class
    def __init__(self,name):
        self.name=name

    def fun(self):                                        #initialising a method()
            print(f"{self.name} I can call ")




class keypad():                       
    def __init__(self,name):
        self.name=name

    def fea(self):
            print(f"{self.name} I am portable ")



class Mobile(Phone,keypad):                                   #inheriting methods from Phone and Keypad class
    def __init__(self,name):
        self.name=name

    def pro(self):
          print(f"{self.name} I can capture Images too ")
          

'''C1=Phone("landline")
C1.fun()'''

'''C2=keypad("Nokia")
C2.fea()
'''

C3=Mobile("Smart phone")
C3.fun()
C3.fea()
C3.pro()


