'''
block of code
run when its called
'''


'''
def func():   # function definition
    print("this is function")  #function body
func()     # function call
'''


'''
def hi(a,b,c):      #parameters(a,b,c)
    print(a,b,c)
hi(1,2,4)           #arguments(1,2,4)
'''


'''
#orbitary arguments
def hi(*a)         # by using star symbol we can acess multiple arguments in single parameters
    print(a)
hi(1,2,4)
'''

#keyword arguments
def hi(**a):         #by using double star symbol we can acess multiple arguments in single parameters in dictionary type
    print(a)
hi(a=1,b=2,c=4)

