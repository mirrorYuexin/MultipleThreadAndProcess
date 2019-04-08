from multiprocessing import Pool
import os, time

def jobForChild(n):
    print('process %s start working'%(os.getpid()))
    time.sleep(n)
    print('process %s has finished it\'s job'%(os.getpid()))

if __name__ == '__main__':
    print('main process %s'%(os.getpid()))
    p = Pool(2)
    for i in range(10):#use the spare process in the pool to do new job
        p.apply_async(jobForChild, args=(i,))
    p.close()
    p.join()
    print('main process finished')
