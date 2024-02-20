import threading, time
from datetime import datetime

def sleeper(i):
    print("hello from %d" %i)
    time.sleep(i)
    print("bye from %d" %i)

print(datetime.now().strftime("%H:%M:%S"))
'''sleeper(0)
sleeper(1)
sleeper(2)
sleeper(3)'''


'''
threading.Timer(1, sleeper, [2]).start()


threading.Thread(target=sleeper, args=(11,)).start()
threading.Thread(target=sleeper, args=(1,)).start()
threading.Thread(target=sleeper, args=(2,)).start()
threading.Thread(target=sleeper, args=(3,)).start()

print(datetime.now().strftime("%H:%M:%S"))


'''
''''

stop = False

def input_thread():
    global stop
    while True:
        user_input = input(" stop?")
        print("user says {}".format(user_input))
        if user_input == "yes":
            stop=True
            break

def output_thread():
    global stop
    count = 0
    while not stop:
        print(count)
        count+=1
        time.sleep(1)

t1=threading.Thread(target=input_thread).start()
t2=threading.Thread(target=output_thread).start()

'''



data_lock = threading.Lock()
data = [x for x in range(6)]

def sync_consume_thread():
    global data, data_lock
    while True:
        data_lock.acquire()
        if len(data) > 0:
            print(threading.current_thread().name)
            print(data.pop())
        data_lock.release()

threading.Thread(target=sync_consume_thread).start()
threading.Thread(target=sync_consume_thread).start()