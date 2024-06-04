import camelcase
x = "this is a practice string with lots of info in it"
c = camelcase.CamelCase()
print(c.hump(x))
