import subprocess

# generate a child process belong to other process
def normalOrder():
    print('execute the linux order')
    r = subprocess.call(['ls', './'])
    print('Exit code:', r)

def orderNeedInput():
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    #nslookup
    #set q=max
    #python.org
    #exit
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)


if __name__ == '__main__':
    normalOrder()
    orderNeedInput()
