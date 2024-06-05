#finding the missing number from a sequence
a = [4,5,7,8]
a[0]=a[0]+1
if a[0] == a[1]:
     a[0]=a[1]
else:
        b=a[0]-1
        print("the missing number is ", b)