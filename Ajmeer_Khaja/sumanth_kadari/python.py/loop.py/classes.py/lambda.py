#creating a lambda function 
sum = lambda x,y :x+y
print(sum(5,5))

#using lambda, filter , printing even numbers
numbs = [2,24,5,1,3,55,7,6,2]
evens = list(filter(lambda n : n%2==0, numbs))
print(evens)

#map function
num = [1,2,3,4,5]
squared = map(lambda x: x**2)