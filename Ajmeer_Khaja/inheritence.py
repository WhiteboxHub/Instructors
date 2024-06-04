# class animals:
#     def __init__(this,name,type):
#         this.name = name;
#         this.type = type;
#     def __str__(this):
#         return f"This is a {this.type} named {this.name}"
#     def printinfo(this):
#         print(this.name,"is a",this.type);

# a1 = animals("scout","dog");
# print(a1);
# a1.printinfo();

# class petanimals(animals):
#     def infoofanimal(this):
#         print(f"{this.type} is a pet animal")

# class wildanimals(animals):
#     def animalinfo(this):
#         print(f"{this.type} is a wild animal");


# p1 = petanimals('scar','cat');
# p1.printinfo();
# p1.infoofanimal();

# p2 = wildanimals('sheru','lion')
# p2.printinfo();
# p2.animalinfo();



class Emplooy:
    def __init__(self,name,id):
        self.name=name;
        self.id=id;
    def __str__(self):
        # print(f"{self.name},{self.id}")
        return f"{self.name},{self.id}"
class Programmer(Emplooy):
    def __init__(self, name, id,role):
        super().__init__(name, id)
        self.role=role;
    def printinfo(self):
        print(f"{self.name} is a {self.role}")

emp1 = Emplooy('aka',9978);
emp2 = Programmer('jack',12431,'full stack Dev');

print(emp2);
emp2.printinfo();