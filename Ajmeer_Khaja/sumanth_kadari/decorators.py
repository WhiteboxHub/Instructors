#decorators
#print even numbers only otherwise show enter even numbers
def extra_add(f):
    def inner(x,y): #wrapper function
        if x%2==0 and y%2==0:
            f(x,y)
        else:
            print("enter a even number")
    return inner

#here im addind decorator 
@extra_add
def add(a,b):
    print(a+b)
add(5,4)