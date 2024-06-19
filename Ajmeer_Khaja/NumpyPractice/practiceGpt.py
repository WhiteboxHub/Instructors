
from dataclasses import dataclass
import numpy as np
from numpy import random
#question :- Take a list of integer as input and convert the it into list of string with same value and print the str list

def Int_to_str(intlist):
    strlist = []
    for i in range(len(intlist)):
        strlist.append(str(intlist[i]))
    print(strlist)
Int_to_str([1,2,3,1,22,331,334,42,23,55,22])
def asending(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[j]<list[i]:
                list[i],list[j]= list[j],list[i]
    print(list)
def sqrtpl(tpl):
   
    print( tuple(x*x for x in tpl))
asending([3,4,2,4,5,6,2,3,6])
sqrtpl((11,22,44,1,2,3,4))
def listofCommon(l1,l2):
    newlst = []
    for ele in l1:
        for ele1 in l2:
            if ele == ele1:
                newlst.append(ele)
    print(newlst)
listofCommon([1,3,2,4,5,6,6,3,3,4],[3,15,26,24,346,2,3,6,2])
def fibinochi(n):
    first = 0
    second = 1
    print(first)
    print(second)
    for i in range(n-2):
        next = first+second
        first = second
        second=next
        print(next)
fibinochi(10)
class rec:
    def __init__(self,length,bredth):
        self.length = length
        self.bredth= bredth
    def __str__(self):
        return f"The rectangle lenght and breath are {self.bredth} and {self.bredth}"
    def area(self):
        area1 = self.length*self.bredth
        return f"The area of rectangel = {area1}"
    def parameter(self):
        para = 2*(self.length+self.bredth)
        return f"The paramater of rect is {para}"
r1 = rec(10,20)
print(r1.area())
print(r1)
print(r1.parameter())
class squre(rec):
    def __init__(self,side):
        super().__init__(side,side)
s1 = squre(3)
print(s1)
print(s1.area())
print(s1.parameter())


@dataclass
class person:
    name:str
    age:int
class users(person):
    
    def newuser(self):
        print(f"The user is {self.name} and age is {self.age}")


p1 = users('User1',24)
print(p1)
p1.newuser()


nparr = np.array([1,2,3,4,5,2,2,32,23,34,321,234,342,354])
print(nparr)

znp = np.zeros((3,3))
onp = np.ones((2,4))


print(np.max(nparr))
print(np.min(nparr))
print(np.median(nparr))
print(nparr.shape)
print(znp.shape)


rint = np.random.randint(10,50,size=(2,3))
print(rint)

npfloat = np.random.rand(4,4)
print(npfloat)

lsp = np.linspace(0,10,5)
print(lsp)

rnp = np.arange(0,20,3)
print(rnp)

