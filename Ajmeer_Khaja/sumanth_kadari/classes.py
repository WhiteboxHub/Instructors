class computer:
    def config(self):
        print("i3","16GB",44)

#creating a object here
com1=computer()
com2=computer() #we can create no.of obj to one class
#so here im calling config function/method
com1.config()
com2.config()

#__INIT__Method----------------------->
class computer:
    #here creating  init /constructor inside im attributes/variables
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    #creating one function/method
    def config(self):
        print("myConfig are",self.cpu ,self.ram)

com1=computer("i4",'16gb')
com2=computer("i4","16GB")

com1.config()
com2.config() 