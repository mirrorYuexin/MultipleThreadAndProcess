from multiprocessing import Manager, Pool
from multiprocessing.managers import BaseManager
import multiprocessing
import time
import os

"""
This is a group of workers for the distributedDemo
"""
class QueueManager(BaseManager):
    pass

# workers do the job
def job(q):
    print('doing job')
    time.sleep(2)
    print('job finished')
    #put the result into the sharing queue
    q.put(os.getpid())

if __name__ == '__main__':

    """
    register the result queue getting function on the network and 
    get it from the manager machine
    """
    QueueManager.register('get_resQueue')
    serverIp = '127.0.0.1'
    print('connect to server: %s'%(serverIp))
    m = QueueManager(address=(serverIp, 1111), authkey=b'123')
    multiprocessing.current_process().authkey = b'123'
    m.connect()
    #get the sharing queue from the network
    q = m.get_resQueue()

    #define 5 workers
    p = Pool(5)
    #start working
    for i in range(5):
        p.apply_async(job, args=(q,))
    #no more workers
    p.close()
    #main process wait for the child process
    p.join()
    print('all jobs finished-------')


