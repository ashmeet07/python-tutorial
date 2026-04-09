import threading
import time

def task(name):
    print(f"Task {name} started")
    time.sleep(2)
    print(f"Task {name} finished")


t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))

t1.start()
t2.start()

t1.join()#ensure syncronization with proper concurrent execution of threads
t2.join()

print("Main thread finished")


#Due to GIL python makes only one thread executes at a time and makes the memory mangement using reference counting