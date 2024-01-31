# KEYWORD ARGUMENTS : HOW TO PRINT DICTIONARIES

def person(**data):         #if we use single star it will print like tuple,here no key value pairs
  # print(data)             #if we use double star we it will print like dictionaries, here we can see key value pairs
    for k,v in data.items():  #here i want print line by line so i will use for loop
     
     #i have printed this code it will printed sucessfully
        #but i want an output in a order , so iam using conditional stmts 
       if k =='firstName' or k =='lasttName' :
        print (k,' :' ,v)
       elif k == 'age':
        print(k, '       :' ,v)
    else:
        print(k, '    :',v)


person(firstName='saketh' , lasttName='ulasa' , age=22 , mobile= 789358)



