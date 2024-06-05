

### decotaror function 


def deco(fun):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return fun(a,b)
    return inner

@deco
def div(a,b):
    print(a/b)
div(2,4)

@deco
def sub(a,b):
    print(a-b)

sub(2,4)

























"""def my_dec(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_dec
def say_hello():
    print("Hello!")

say_hello()
"""