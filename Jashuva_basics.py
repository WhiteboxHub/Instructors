#Basics of Python practise session

My_First_variable=5          # Creating Global variables using the snake case naming
X="hello world" 
Text= "This is a \"Text\" "
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
print(Text)    # using Escape char

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

My_dic()