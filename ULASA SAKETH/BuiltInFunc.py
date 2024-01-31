import math


#creating a list of numbers
#finding min and max values in the list
#for the we have some built in functions called min and max

a = [1,22,32,51,43,77,88,83,90,99]
minval=min(a)
maxval=max(a)
print(minval)
print(maxval)


#here iam going to use some fuctions to check the power of a number

x=pow(4,10)
print(x)


#here i want an absolute value 
#like i entered negative value, by using one function we will get positive value

b=abs(-12.22)
print(b)


#here i want to find squareroots
#for that we need to import math module first

v=math.sqrt(9)
print(v)


#here i dont dont want numbers which is in decimals

u=math.floor(1.222)     #floor is used to break the numbers after the dot
print(u)
i=math.ceil(2.888)      #ceil is used to break the numbers after the dot, and it will give round figure value
print(i)


