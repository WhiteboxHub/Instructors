import re
a = 'my name is bunny, and my age is 23'
b = re.findall(r'\Bme',a)             #spl sequences \A,\Z,\s,\S,\d,\D,\w,\W,\b,\B'''      
print(b)
