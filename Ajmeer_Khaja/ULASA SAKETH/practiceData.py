def person(**data):
    print(data)
    for k,v in data.items():
        if k=='Fname' or k=='Lname' :
         print(k,' :',v)
        elif k=='age':
         print(k,'   :',v)
        else:
         print(k,':',v)

Fname=input("enter your first name :")
Lname=input("enter your last name :")
age=input("enter your age :")
mobile=input("enter your mobile number :")

person(Fname=Fname,Lname=Lname,age=age,mobile=mobile)