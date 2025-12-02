import threading
counter=0
def increase_counter():
    global counter
    for i in range(100000):
        counter+=1
    

def decrease_counter():
    global counter
    for i in range(100000):
        counter-=1
    

t1=threading.Thread(target=increase_counter)
t2=threading.Thread(target=decrease_counter)
t1.start()
t2.start()
t1.join()
t2.join()
print("the finale number is: ",counter)