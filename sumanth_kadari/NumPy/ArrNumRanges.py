import numpy as np

#arange function()
a=np.arange(0,12,2,dtype="int")
print(a)

#linspace function()
a=np.linspace(0,20,5,endpoint=19,retstep=True,dtype=int)
print(a)


#logspace function()
a=np.logspace(0,10 ,endpoint=False,base=2)
print(a)
