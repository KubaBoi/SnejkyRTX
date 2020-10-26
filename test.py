from multiprocessing import Pool, TimeoutError
import time
import os

arr = []
for i in range(50):
    arr.append(-5)

def f(x):
    global arr
    return x + arr[x]

if __name__ == '__main__':
    t = time.time()

    # start 4 worker processes
    with Pool(processes=4) as pool:
        print(pool.map(f, range(50)))

        res = pool.apply_async(os.getpid, ())           

        # launching multiple evaluations asynchronously *may* use more processes
        #multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]

        # make a single worker sleep for 10 secs
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("We lacked patience and got a multiprocessing.TimeoutError")

        print("For the moment, the pool remains available for more work")

    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")
    print("time: " + str(time.time() - t))