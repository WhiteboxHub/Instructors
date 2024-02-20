#creating a square with star symbol
print("Square pattern")
for i in range(4):
    for j in range(4):
        print("* ",end="")
    print()
    
#left reacangle triangle
print("Left Reacangle triangle")
for i in range(4):
    for j in range(i):
        print("* ",end="")
        print()