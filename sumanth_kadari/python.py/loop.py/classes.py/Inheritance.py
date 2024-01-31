class csstudent:
    #class variables
    stream="cse"
    #init method or constructor
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        #function/method
    def details(self):
        print("hey mySelf",self.name,"and my id is",self.roll)
 #creating a obj       
student1=csstudent("sumanth",22)
student1.details()
print(student1.stream)

#here i am creating another class/child classs
class ecstudent(csstudent):
    #stream1="ec"
    pass
ec=ecstudent("Rahul",33)
ec.details()
print(ec.stream)