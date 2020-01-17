import threading
import time

local_school = threading.local()
global_school = 1


def func():
    global local_school
    global global_school
    for j in range(100):
        local_school = j
        print('%s>>>%s>>>local>>>>%s' % (threading.current_thread().name, j, local_school))
        global_school = j
        print('%s>>>%s>>>global>>>>%s' % (threading.current_thread().name, j, local_school))


for i in range(3):
    t = threading.Thread(target=func, name='thread' + str(i))
    t.start()

time.sleep(5)
