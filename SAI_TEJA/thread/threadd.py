import threading
import time

def square(n):
    print('square of a number is:')
    for i in n:
        time.sleep(0.2)
        print('square is :',i*i)

def cube(n):
    print('cube of a number is:')
    for i in n:
        time.sleep(0.2)
        print('cube is :',i*i*i)

r= time.time()
l = [1,2,3,4,5]
t1=threading.Thread(target=square,args=(l,))
t2=threading.Thread(target=cube,args=(l,))
t1.start()
t2.start()
t1.join()
t2.join()
print('time taken to excute two functions:',time.time()-r)