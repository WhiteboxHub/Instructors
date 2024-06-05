#creating a function here
def extra_add(f):
    def inner(x,y):     #wrapper class its xtra behaviour to the original fun
        if x%2==0 and y%2==0: #if the cndtion is met,original func is called
            f(x,y)
        else:
            print("enter a even numbers")
    return inner        #decorators will return inner fun ,will be replacing originl func

#onemore function
@extra_add             
#applying decorators
def add(x,y):
    print(x+y)
add(2,4)



    