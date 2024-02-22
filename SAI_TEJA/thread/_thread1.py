import _thread
import time
def name(n):
    time.sleep(0.5)
    print("my name is:",n)
def country(m):
    time.sleep(0.5)
    print("my country name is:",m)
r = time.time()
_thread.start_new_thread(name,("bunny",))
_thread.start_new_thread(country,("india",))
print('the time taken to execute two functions',time.time()-r)