import threading
import concurrent.futures as cf
import time

counter = 0
counter_lock = threading.Lock()

def external_function():
    c = external_count()


def external_count():
    global counter
    with counter_lock:
        counter = counter + 1
        return counter

#Sample function for test purposes
def computing5s(thr_id):
    time.sleep(5)
    external_function()

    return thr_id, thr_id*thr_id

def init_values(f):
    f_values={}

    #Between BEGIN and END there is too slow solution.
    #Rewrite the solution to utilize parallelism
    #
    #BEGIN
    ## starts dictionary with return values from function f
    futures = []
    with cf.ThreadPoolExecutor(max_workers=50) as executor:
        for i in range(50):
            future = executor.submit(f, i)
            futures.append(future)
            #idx, val=f(i)
            #f_values[idx]=val

    f_values = {future.result()[0]:future.result()[1] for future in cf.as_completed(futures)}


    #END
    print("count = ", counter)
    return f_values


#Test software under this if
if __name__ == "__main__":
    ret=init_values(computing5s)
    print(ret)
