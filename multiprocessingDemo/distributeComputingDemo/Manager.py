from multiprocessing import Manager, Pool
import multiprocessing
from multiprocessing.managers import BaseManager
import time, os

# quality controller check the job finished by workers
def checkJob(q):

    while True:
        try:
            res = q.get(timeout=3)
            print('%s\'s job checked by %s!' % (res, os.getpid()))
        except BaseException as e:
            if q.empty() == True:
                waitingTime = 0
                for i in range(10):
                    time.sleep(1)#no job to check, wait for 1 s
                    waitingTime = waitingTime + 1
                    print('waited for %d s'%(i))
                    if q.empty() != True:
                        break #new job finished, break the waiting loop
                if q.empty() == True and waitingTime > 9:
                    break#no job came after 10s, break the while loop

# workers do the job
def job(q):
    print('doing job')
    time.sleep(2)
    print('job finished')
    q.put(os.getpid())# tag the job with worker's id


class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    #define the task and result queue
    task = Manager().Queue()
    result = Manager().Queue()
    #register the queues to network
    QueueManager.register('get_taskQueue', callable=lambda:task)
    QueueManager.register('get_resQueue', callable=lambda:result)
    manager = QueueManager(address=('', 1111), authkey=b'123')
    multiprocessing.current_process().authkey = b'123'#to avoid some odd problems
    manager.start()

    #just use result queue in this demo
    # tasks = manager.taskQueue()
    q = manager.get_resQueue()

    #define 5 workers and 3 checkers
    workers = Pool(5)
    checker = Pool(3)

    #start working
    for i in range(5):
        workers.apply_async(job, args=(q,))
    #start checking
    for j in range(3):
        checker.apply_async(checkJob, args=(q,))
    #no more works and checkers from main process
    workers.close()
    checker.close()
    #main process wait for the child process-workers and checkers
    workers.join()
    checker.join()
    #worker and checker finished their job
    manager.shutdown()
    print('all done!')
