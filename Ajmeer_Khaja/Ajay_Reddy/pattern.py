#creating a square with star symbol
print("Square pattern")
for i in range(4):
    for j in range(4):
        print("$ ",end="")
    print()
    
#left reacangle triangle
print("rightangle triangle")
for i in range(4):
    for j in range(i+1):
        print("* ",end="")
    print()
#down reacangle triangle
print("down rightangle triangle")
for i in range(4):
    for j in range(4-i):
        print("* ",end="")
    print()