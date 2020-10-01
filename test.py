import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    a = 0
    for i in range(0, 5000000):
        a += 1
    logging.info("Thread %s: finishing", name)

t = time.time()
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    for index in range(4):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)

print(time.time() - t)