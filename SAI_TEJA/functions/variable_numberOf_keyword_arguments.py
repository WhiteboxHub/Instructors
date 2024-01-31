def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)


person('bunny',age=23,country='united states',mobile=00000)