from threading import *
import time

class Apple(Thread):
    def run(self):
        for i in range(10):
            time.sleep(1)
            print("apple")

class Orange(Thread):
    def run(self):
        for i in range(10):
          time.sleep(1)
        print("orange")

a=Apple()
b=Orange()

Stime=time.perf_counter()
a.start()
b.start()
a.join()
b.join()
Etime=time.perf_counter()

print(f'proceed in {round(Etime-Stime)} seconds')