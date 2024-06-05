#--------using filter() function
#--------using filter() to print the even numbers from the given list

a=(1,2,3,4,5,6,7,8,9)

def fun(i):
    if i%2==0:
        return True
result = filter(fun, a)
print (list(result))


#----------filter() function example
a = 'abcdefghijklmnopqrstuvwxyz'

def fun(i):
    if i not in 'aeiou':
        return True

    result = filter(fun, a)
    print (list(result))
