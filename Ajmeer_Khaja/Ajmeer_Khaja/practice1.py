def statemen(a,b):
    if(a>b):
        return True;
    else:
        return False;
    

ans = statemen(8,10);
print(ans);


def singlelineStatement(a,b,c,d):
    print("a is greate") if a>b else print('b is greater than a')
    print(a,'b',c,d)


singlelineStatement(1,23,4,2)