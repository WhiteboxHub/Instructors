#Arm Strong Code by useing loops and if else condition
"""n=int(input("enter the number to check Arm_Strong or Not"))
temp = n
sum = 0
while n > 0:
    rem = n%10
    sum = sum + rem*rem*rem
    n=n//10
if temp == sum:
    print("arm strong")
else:
    print("not an arm strong")"""
# ArmStrong by useing function
n = int(input("enter any number to check it is armstrong or not \n"))
def checkArm(num):
    sum =0 
    temp = num
    while(num!=0):
        rem = num%10
        sum = sum + rem*rem*rem
        num = num//10
    """if(temp==sum):
         yield "armStrong"    # by useing generator
    else:
         yield "not an armstrong"
result = checkArm(n)
for i in result:  #useing generator
 print(i)"""
    if(temp==sum):
         return "armStrong"      # by useing retuen method
    else:
         return "not an armstrong"
result = checkArm(n)
print(result)