#local space = creating a variable inside the function or printing inside the function only
   #            we cant use thevariable at outside

'''

def hello():
    x='hi'         # creation of varible
    print(x)       # printing the variable
hello()    

'''
#calling the variable at outside

def sam():
    x='hello'
    return x     #by using return it will gives x value
a=sam()          #by assigning the fuction for a it will gives x value
print(a)