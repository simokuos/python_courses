import threading
import concurrent.futures as cf
import time

#heavy_computing for test purposes!
#You may modify the function if necessary
if __name__ == "__main__":
    def heavy_computing(idx):
        print('->heavy_computing('+str(idx)+')')
        time.sleep(10)
        print('<-heavy_computing('+str(idx)+')')
        return idx, idx*idx

def start_threads(f, N):
    #starts funktion f(idx) N säikeeseen
    futures = []
    with cf.ThreadPoolExecutor() as executor:
        for idx in range(N):
            future = executor.submit(f, idx)
            futures.append(future)

    return futures

def wait_threads(th_list):
    ordered_list = [ future.result() for future in cf.as_completed(th_list) ]
    ordered_list.sort()
    value_list = [value for (x, value) in ordered_list]
    return value_list

#Test software under this if
if __name__ == "__main__":
    N=10

    print('None started')
    th_list=start_threads(heavy_computing, N)
    print('Wait...')
    ret=wait_threads(th_list)
    print('All futures completed')
    print(ret)
