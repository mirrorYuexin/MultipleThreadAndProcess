from multiprocessing import Process
import os,time

def jobForChild(str=None):
    print('process %s is working and say %s'%(os.getpid(), str))
    time.sleep(2)
    print('work finished')

if __name__ == '__main__':
    p = Process(target=jobForChild, args=('hi', ))
    p.start()
    # without join() main process will move on
    # when main process finished, child process will keep alive
    p.join()
    print('main process finish')