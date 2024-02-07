#Basics of Python practise session

My_First_variable=5          # Creating Global variables using the snake case naming
X="hello world" 
Text= "This is a \"Text\" "     # using Escape char
print(My_First_variable,X)   

def My_Exp():
 A,B,C= "assigned", "values","to variables" # assigning multiple values to multiple variables (local variables)  
 P=1+5j # complex Number 
 Q=int(1.0)  # casting from float to int
 R=float(1)  # casting from int to float
 print( A,B,C) 
 print(P,Q,R)

My_Exp()

# String Operations

print(X[0:5])    # Printing a part of string using Index
print(len(X))    # len of string
print(X.upper())  # converting to upper case
print(Text)    

# list []

def My_list():
 First_list=["apple", "banana" ,"Orange"]
 Second_list=["These are the " "names of " ]
 print(First_list[0])  # printing a part of List
 First_list.insert(2,"watermelon")   #inserting Str in List
 First_list.extend(Second_list)      # extending list
 First_list.append("Fruits") # appends the list 
 print(First_list)

My_list()   

# Tuple ()
def My_tuple():
 First_tuple=tuple((2,3,4))    # tuple constructor
 Second_tuple=list(First_tuple)    # converting from tuple to List to modify tuple
 Second_tuple[0]=1                  # adding value to list   
 First_tuple=tuple(Second_tuple)    # converting to tuple
 print(First_tuple)
 print(len(First_tuple))  #len of tuple

My_tuple()

#sets {}

def My_sets():  
 this_is_set= {"apple", "banana", "cherry"}
 print(this_is_set)

My_sets()

# dict 

def My_dic():
 My_car= {
  "brand": "Ford",
  "model": "Fiesta",
  "year": 2012          
 }
 print(My_car["model"])
 My_car.update({"year":2023})     #updating DICT
 My_car.pop("brand")
 print(My_car["year"])

My_dic()

#IF - else using Functions

def Con(H,I): #used two parameters

 if H > I : 
  print(f"{H} is greater than  {I}"  )   #used String formatter to print the value of Input given 
 elif H < I:
  print(f"{H} is lesser than {I}",)
 else: print(f"{H} is Equal to {I}",)  

Con(50,50)  # arguments for Functions

#nested If else to check if the given value is greater than 10 

def nes(Y):
 if Y>10: 
    print(f"{Y} is greater than 10") 
    if Y>20: 
      print(f"{Y} is greater than 20")
    elif Y == 20:                              #using else -if
        print(f"{Y} is equal to 20")
 else:print(f"{Y} is lesser than 10")

nes(20)


#loops  (While and for)

def Wloo():
  i=1
  while i<20 :                 #using while loop
    print(i)
    i=i+1                      #increment operator
Wloo()  


def Floo():                               
  cars=["vento","virtus","slavia","octavia"]      
  for x in cars:                                   #using for loop
   print(x)

Floo()