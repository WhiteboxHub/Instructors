class students:
    def __init__(self,name,age,cls,rollno):
        self.name =name;
        self.age = age;
        self.cls= cls;
        self.rollno=rollno;
    def __str__(self):
        return f"{self.name} of age {self.age} studying in class {self.cls}"

st1 = students('khaja',13,7,1)
print(st1.rollno);
print(st1);
del st1.cls;
print(st1)