from threading import *
import time
class apple(Thread):
    def run(self):
     for i in range(10):
        time.sleep(1)
        print("apple")

class orange(Thread):
    def run(self):
      for i in range(10):
        time.sleep(1)
        print("orange")
a=apple()
b=orange()
a.start()
b.start()
'''a.join()
b.join()'''