x =20
y=10
try:
    print(x+y)
except NameError:
    print('Variable not declared',NameError)
except:
    print('some thing went wrong')
else:
    print('everything went perfectly')