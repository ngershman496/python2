from multiprocessing.connection import wait
import psutil


# display user, current OS and its properties
def find_operating_system():
    if psutil.WINDOWS:
        return 'Windows'
    elif psutil.LINUX:
        return 'Linux'
    elif psutil.MACOS:
        return 'Mac'
    elif not psutil.WINDOWS and not psutil.LINUX and not psutil.MACOS:
        return 'Unknown'


def get_current_user():
    u = psutil.users()
    print('Current User:\t', u[0][0])
    print('Terminal:\t', u[0][1])
    

# display the user all users on the machine and their attributes

def get_all_users():

    u = psutil.users()
    num_users = len(u)
    # print(num_users)
    
    print('All Users:')
    for n in range (num_users):
        print('\tUser:\t', u[n][0])
        print('\tTerminal:', u[n][1])
        	

# display short list of running processes

def show_processes():
    print('First 20 Processes:')
    x = 0
    for proc in psutil.process_iter(['pid','name','username']):
        if x < 20:
            print(x+1 ,' ', proc.info)
            x = x + 1
        else:
            break

def process1():
    print('Process Started')

def invoke_process():
    
    proc = psutil.Popen(["python", "-c", "print('I started')"])
    return proc.pid
    
    
def kill_process(id):
    if psutil.Process(id).is_running():
        print('Process ', id, ' is running...\nProceeding to kill')
        proc = psutil.Process(id)
        proc.kill()
        proc.wait()
        print('Process Killed Successfully')
    else:
        print('Process ', id, ' is not running')
    

if __name__ == '__main__':
    import time


    print('Operating System:',find_operating_system())
    get_current_user()
    get_all_users()
    show_processes()
    proc_id = invoke_process()
    #time.sleep(1)
    kill_process(proc_id)
    