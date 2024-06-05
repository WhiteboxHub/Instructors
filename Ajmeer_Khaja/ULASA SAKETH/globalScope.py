#globalScope = calling the variables outside the function

x=10
y=20

def func():
    global x     # by using global keyboard we can print outside the function 
    x=100        #if we wont use global keyboard it will print the variable which we assigned before function
    global y
    y=200

    print('inside function = ' ,x)
    print('inside function = ' ,y)
func()
print('outside function = ' ,x)
print('outside function =' , y)