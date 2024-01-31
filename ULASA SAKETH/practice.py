def person(**data):
    #print(data)
    for k , v in data.items():
        if k=='fname' or k=='lname':
            print(k,' :',v)
        elif k=='age':
            print(k,'   :',v)
        else :
            print(k,':',v)
       
fname=input("enter you fname :")
lname=input("enter your lname :")
age=input("enter your age :")
mobile=input("enter your mobile :")
print("")
person(fname=fname,lname=lname,age=age,mobile=mobile)