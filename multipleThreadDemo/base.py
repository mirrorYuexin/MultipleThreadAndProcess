import threading
import time

def jobA(n=0):
    for i in range(n):
        print('now the thread N0.%s is doing job A'%threading.current_thread().name)
        time.sleep(2)# do a 2s-job, total time consume 2*n s for one job

def jobB(n=0):
    for i in range(n):
        print('now the thread N0.%s is doing job B'%threading.current_thread().name)
        time.sleep(2)# do a 2s-job, total time consume 2*n s for one job

def doJob(n=0):
    thread1 = threading.Thread(target=jobA, args=(n, ), name='thread 1')
    thread2 = threading.Thread(target=jobB, args=(n, ), name='thread 2')

    thread1.start()
    thread2.start()
    # if there is no join, main thread will finish without child thread's job finish
    thread2.join()
    thread1.join()

if __name__ == '__main__':
    # do job A and B by one worker(thread)
    begin = time.time()
    jobA(2)
    jobB(2)
    end = time.time()
    print('total time:%.2fs for one worker' % (end - begin))

    # do job A and B by two workers(threads)
    begin = time.time()
    doJob(2)
    end = time.time()
    print('total time:%.2fs for two workers'%(end-begin))