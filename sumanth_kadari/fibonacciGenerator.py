def fibonacciGen():  #defining a function
  
    a,b=0,1         #taking Attributes
    
    while True:    #until the condition satisfy
        yield a
        
        a,b= b,a+b   #fibonacci increases
        
fib=fibonacciGen()   #crea
for i in range(10):
    print(next(fib))       
        
    