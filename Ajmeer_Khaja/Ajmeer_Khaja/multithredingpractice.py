import threading
import time

def sleeptime(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds) 
    print(f"awake after {seconds} sec of sleep")

# sleeptime(3)
# sleeptime(6)
# sleeptime(9)

t1 = threading.Thread(target=sleeptime,args=[3])
t2 = threading.Thread(target=sleeptime,args=[6])
t3 = threading.Thread(target=sleeptime,args=[9])

t1.start()
t2.start()
t3.start()
