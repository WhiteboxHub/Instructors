#addition 
#with even numbers
'''

def extra_add(f):
    def inner(x,y): 
        if x % 2 == 0 and y % 2 == 0:
           f(x,y)
        else:
         print("write even numbers")
    return inner

@extra_add
def add(a,b):
    print(a+b)
add(1,8)

 '''

#multiplication
#even numbersx
'''

def moreCode(f):
    def inner(x,y):
        if x%2 == 0 and y%2 == 0 :
            f(x,y)
        else:
            print("write even")    
    return inner

@moreCode
def multi(a,b):
    print(a*b)
multi(2,6)    

'''
#subtraction
#if greater than given number

def extra_sub(add):
    def inner(x,y):
        if x>3 and y>1:
            add(x,y)
        else:
            print("none") 
    return inner           

@extra_sub
def sub(a,b):
    print(a-b)
sub(7,2)    