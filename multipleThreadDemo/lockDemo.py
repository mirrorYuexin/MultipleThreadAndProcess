import threading
import numpy as np
import time

publicFigure = 0
lock = threading.Lock()

def changeFigureWithoutLock(n=0):
    global publicFigure
    # to enhance the probability of error
    print(threading.current_thread().name, 'begin')
    temp = publicFigure + n
    time.sleep(n)
    publicFigure = temp
    time.sleep(n)
    publicFigure = publicFigure - n
    print(threading.current_thread().name, 'end')

def changeFigureWithLock(n=0):
    global publicFigure
    lock.acquire()
    try:  # to avoid permanent lock causing by function inner error
        # to enhance the probability of error
        print(threading.current_thread().name, 'begin')
        temp = publicFigure + n
        time.sleep(n)
        publicFigure = temp
        time.sleep(n)
        publicFigure = publicFigure - n
        print(threading.current_thread().name, 'end')
    finally:
        lock.release()



def do():
    global publicFigure
    thread1 = threading.Thread(target=changeFigureWithoutLock, args=(1, ), name='thread 1')
    thread2 = threading.Thread(target=changeFigureWithoutLock, args=(2, ), name='thread 2')

    thread1.start()
    thread2.start()

    thread2.join()
    thread1.join()

    print('final value of publicFigure:%s (without lock)'%(publicFigure))
    # init the globalFigure
    publicFigure = 0

    thread1 = threading.Thread(target=changeFigureWithLock, args=(1, ), name='thread 1')
    thread2 = threading.Thread(target=changeFigureWithLock, args=(2, ), name='thread 2')

    thread1.start()
    thread2.start()

    thread2.join()
    thread1.join()

    print('final value of publicFigure:%s (with lock)'%(publicFigure))



if __name__ == '__main__':
    do()
