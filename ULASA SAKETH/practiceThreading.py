from threading import*
import time

class Orange(Thread): 
    def run(self):
        for i in range(10):
            time.sleep(1)
            print("orange is for you")
         

class Apple(Thread):
    def run(self):
        for i in range(10):
            time.sleep(1)
            print("apple is for you")
a=Orange()
b=Apple()
a.start()
b.start()