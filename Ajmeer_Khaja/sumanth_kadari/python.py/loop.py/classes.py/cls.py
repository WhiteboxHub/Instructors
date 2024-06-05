class Computer:
    #init method or constructor
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    #creating function
    def config(self):
        print("computer name is",self.name,"and id is",self.id)
    
#creating instance for class
com1=Computer("Dell",22)
com2=Computer("HP",33)

com1.config()
com2.config()
