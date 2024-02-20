#Arm Strong Code by useing loops and if else condition
n=int(input("enter the number to check Arm_Strong or Not"))
temp = n
sum = 0
while n > 0:
    rem = n%10
    sum = sum + rem*rem*rem
    n=n//10
if temp == sum:
    print("arm strong")
else:
    print("not an arm strong")
