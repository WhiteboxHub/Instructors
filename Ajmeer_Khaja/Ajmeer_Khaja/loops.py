length = 44;
# for i in range(length):
#     print(i);
# while i>1:
#     print(i);
#     i-=1;
myList = [11,33,12,34,52,34,53,23,88,983,8294,83,83,33,9034];
for i in myList:
    if(i>100):
        print(i);
    else:
        continue;

for i in range(len(myList)):
    if(myList[i]>100):
        print(f"The number {myList[i]} is greater than 100")
    else:
        continue;