#---------------CREATNG A DICTIONARY AMD SORTING THE VALUES
keys = ['navin' , 'harsh' , 'kiran'  ]
values = ['python', 'java' , 'js']
data= dict(zip(keys,values))
print(data)
data ['monika'] = 'c#'
print(data)
del data ('monika')
print (data)

#--------lambda exp - even numbers greater than 50
numbers = [11 ,20 ,31, 40 , 51 , 60]
even = list (filter ( lambda x : x%2 ==0 and x > 50 , numbers))
print ( " even numbers >50 :" , even)

#--------lambda exp - even numbers
numbers = [11 ,20 ,31, 40 , 51 , 60]
even = list (filter ( lambda x : x%2 ==0 , numbers))
print ( " even numbers :" , even)

#----------lambda exp - multiplication of a number
f = lambda a : a*a
result = f(5)
print (result)

#------generator functions
# A generator function that yields 1 for first time, 
# 2 second time and 3 third time 
def generator(): 
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generator function 
for value in generator():  
    print(value)

#-------------metaclasses
class mymeta(type):
    pass

class myclass( metaclass = mymeta):
    pass
    class mysubclass(myclass):
        pass
        print (type (mymeta))
                print(type(myclass))
                print(type(mysubclass))

                