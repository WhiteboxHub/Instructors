def Item_pricing(item="laptop",price="29K"):
    print(f"{item}'s price is {price}");

Item_pricing('mobile','10K');
Item_pricing();
Item_pricing(price='5K',item="wriste Watch");
def EmptyFucntion():
    pass;
EmptyFucntion();

x = lambda a: a-19;
print(x(10));

LambdaTest = lambda a,b,c:a*b-c;
print(LambdaTest(1,2,3))

def lamfun(n):
    print(n)
    return lambda a:a*n;
multiplier = lamfun(4)
print(multiplier(22))
