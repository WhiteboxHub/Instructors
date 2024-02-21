# fibinacci series -> 0,1,1,2,3,5,8
a,b=0,1
num = 10
print("the fibinacci series are : ",a,b,end=",")
for i in range(num):
    c=a+b
    a=b
    b=c
    if num<=c: 
     break
    print(c,end=",")
    i=i+1