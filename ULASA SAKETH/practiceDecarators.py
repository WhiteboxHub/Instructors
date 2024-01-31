def extra_add(f):
    def inner(x,y):
     if x%2==0 and y%2==0:
        f(x,y)
     else:
        print("write even numbers")
    return inner
@extra_add
def add(a,b):
    print(a+b)
add(2,4)