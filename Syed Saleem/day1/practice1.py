year=int(input("entr year : "))
def leap_year(year):

    
    if year%4==0:
        print("it is a leap year")
        return True
        
    elif year%100==0:
        return False
    elif year%400==0:
        return True
        
    else:
        print("1990 is not divisible by 4 hence not a leap year")
        return False
        

res=leap_year(year)

print(res)
print(si,__dict__)