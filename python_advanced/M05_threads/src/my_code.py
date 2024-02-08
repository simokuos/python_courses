import threading
import time

#heavy_computing for test purposes!
#You may modify the function if necessary
if __name__ == "__main__":
    def heavy_computing(idx):
        print('->heavy_computing('+str(idx)+')')
        time.sleep(10)
        print('<-heavy_computing('+str(idx)+')')

def start_threads(f, N):
    thlist = []
    #starts funktion f(idx) N säikeeseen
    for n in range(N):
        th = threading.Thread(target=f, args=(n,))
        thlist.append(th)
        th.start()

    return thlist

def wait_threads(th_list):
    for th in th_list:
        th.join()

#Test software under this if
if __name__ == "__main__":
    N = 100
    th_list=start_threads(heavy_computing, N)
    wait_threads(th_list)
