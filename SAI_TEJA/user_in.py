def person(fnme,lname,age,mobile):
    print('first name : ',fname)
    print('last name  :',lname)
    print('age        :',age)
    print('mobile     :',mobile)

fname,lname = input('enter the name:').split(',')
age = int(input('age:'))
mobile = int(input('number:'))
person(fname,lname,age,mobile)