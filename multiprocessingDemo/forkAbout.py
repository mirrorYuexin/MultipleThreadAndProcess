import os

print('the main process id:',os.getpid())

"""
fork() will create a child process and return 0 
and child's pid for child and main process respectively
"""
pid = os.fork() # the below code will be executed two times by main and child process

if pid == 0:
    print('child process say hello(pid:%s) and my father is %s'%(os.getpid(), os.getppid()))
else:
    print('main process say hello(pid:%s) and my child is %s'%(os.getpid(), pid))

