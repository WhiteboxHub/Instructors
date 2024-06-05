import threading
import time

def my_function():
    for _ in range(5):
        print(threading.current_thread().name, "is running")            
        time.sleep(1)

# Create and start two threads
thread1 = threading.Thread(target=my_function, name="Thread 1")
thread2 = threading.Thread(target=my_function, name="Thread 2")

thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Main thread is done")

#-------------
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(threading.current_thread().name, i)

def print_letters():
    for letter in 'ABCDE':
        time.sleep(1)
        print(threading.current_thread().name, letter)

# Create two threads
thread1 = threading.Thread(target=print_numbers, name="Thread 1")
thread2 = threading.Thread(target=print_letters, name="Thread 2")

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Main thread is done")


#---------------------------
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for _ in range(5):
            print(threading.current_thread().name, "is running")
            time.sleep(1)

# Create and start two threads
thread1 = MyThread(name="Thread 1")
thread2 = MyThread(name="Thread 2")

thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Main thread is done")


#-------------------------
import threading

import time

def calc_square(numbers):
    print('square number:')
    for number in numbers:
            time.sleep(0.2)
            print('square: ',number* number)
def calc_cube(numbers):
    print('cube number:')
    for number in numbers:
        time.sleep(0.2)
        print('cube:', number*number * number) 

initial_time = time.time()
l = [1,2,3,4,5] 

t1 = threading.Thread(target = calc_square ,args=(1,))

t2 = threading.Thread(target=calc_cube ,args=(1,))

t1.start()
t2.start()

t1.join()
t2.join()
print('Time taken :', time.time() - initial_time)


#------------
from time import sleep
from threading import*

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1= Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Bye")

