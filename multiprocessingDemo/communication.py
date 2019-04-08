from multiprocessing import Process, Queue, Pool, Manager
import os, time

def generateData(q):
    print('worker %s is generating data to queue'%(os.getpid()))
    for i in range(5):
        print('%d in'%(i))
        q.put(i)
        time.sleep(1)

    print('worker %s\'s job finished'%(os.getpid()))

def getData(q):
    while True:
        print('move data %s out from queue'%(q.get()))
        time.sleep(2)



if __name__ == '__main__':
    q = Manager().Queue()

    pool = Pool(8)
    for i in range(8):
        pool.apply_async(generateData, args=(q,))
    # generator = Process(target=generateData, args=(q,))
    pool.close()

    mover = Process(target=getData, args=(q,))
    # generator.start()
    mover.start()
    pool.join()
    # generator.join()
    while True:
        if q.empty() == True:
            break
    mover.terminate()# because the while





