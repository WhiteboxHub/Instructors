#---------------map examples 1 
#function to be applied
def add_two(x):
    return x+2

 #list of integers
 
num = [ 34, 23, 45, 10] 

 #using map() function

mapping = map(add_two, num)  
result = list(mapping)
print(f" final result : {result}.")


# ------------ map() examples 2

def addition(n):
    return n + n
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

#------map() function example 3

sampletuple = ( 1,2,3,4,5,6)
def squarecube(i):
  if i%2==0:
    return i**2
    else:
      return i**3

result = map(squarecube, sampletuple)
print(list(result))