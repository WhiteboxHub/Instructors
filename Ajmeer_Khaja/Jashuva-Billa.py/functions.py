
""" Functional programming
A function is a block of code which only runs when it is called."""

def Jb():   #created a function using def keyword
 print("This is written in a function")

Jb()  #calling a function 

#Arguments and parameters in a Function

def Arg(name,age):   # used argumnets like name and age
 print(f"hello My name is " +name + " and my age is ",age )

Arg("Jashuva",21)  #parameters 
Arg("Kishore",24)  #apassed another parameters and called function again


def fun(name,*Max_speed): #used Arbitary args and provided only two args
 print(f"To print", name, "Specifications and other details ",Max_speed )
  
fun("Scorpio",180,"with max Hp")  #used 3 parameters  (160 and HP (parameters) were assigned to Max_speed using * and convereted to tuple)
fun("Scorpio",160, "in 45 sec", "with max Torque" )  #used 4 parameters


def Cars(car1, car2,car3,car):   # using the Keyword args 
 print("My First car was",car1,)
 print("My Fav car was",car2,)
 print("My dream car was",car3,)
 print("My cars",car,)

Cars(car1='V2',car2="sx",car3="M2", car= "the list goes on",)


def Students(**details,):                           # using the Keyword-args and printing multiple parameters
 print("The name of the student is ",details["Name"], details["std"], ", Roll number is", details["roll"])

Students(Name="Billa",std="X class",roll="16" )


#used the Default keyword in args

def Office(Emp_id,Name,Exp="Fresher"):
 
 print( "The Emp ID is",Emp_id,"," "Name :", Name,"," "Experience is",Exp)

Office(2011,"Jashuva",)



# functions using lambda and communicating between functions   -- simple calcuator (div of two and result div with another variable)

def operation(z):         
 
 div=lambda x,y:x/y     #lambda exp      a,b,c,result,  result= a/b    ,result/c
 result_div=div(92000,6)     #x=92000,Y=6
 print(result_div)           # result_div= 92000/6,    (15333)
 print(result_div/z)

operation(22)



