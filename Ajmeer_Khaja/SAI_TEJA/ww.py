#filter using lambda
number = [10,11,22,3,55,40]
result = filter(lambda num:num%2==0,number)
print(list(result))
