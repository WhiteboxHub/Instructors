#filter
def isEven(num):
    return num%2==0

numbers = [10,20,22,33,50,60,40,10]
result = filter(isEven,numbers)
print(list(result))
