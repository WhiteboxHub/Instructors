class iterator:
     
     def __init__(self):
         self.count=1
         
     def __iter__(self):
         return self
     
     
     def __next__(self,lst):
         if self.count<=19:
             res=self.count
             self.count+=1
             return res
         else:
             raise StopIteration
         
it=iterator()
val=[32,4,3,2,3,2]

print(it.__next__(val))
