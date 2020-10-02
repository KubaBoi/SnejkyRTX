import math
import threading

try:
    from SnejkyEngine.Threading.threadVariables import ThreadVariables
except: #testing
    import os
    import sys

    PACKAGE_PARENT = '..'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
    from Threading.threadVariables import ThreadVariables

class ThreadManager:
    def __init__(self, screenManager):
        self.screenManager = screenManager
        self.threadCount = 3

    def update(self, countOfPixels):
        oneThreadPixels = math.floor(countOfPixels/self.threadCount)

        threads = []
        for i in range(1, self.threadCount):
            x = self.createThread(i, oneThreadPixels)
            threads.append(x)
            x.start()

        #prida se posledni vlakno
        x = self.createThread(self.threadCount, 
                        countOfPixels - (oneThreadPixels * (self.threadCount-1)))
        threads.append(x)
        x.start()

        for index, thread in enumerate(threads):
            thread.join()

    def createThread(self, index, pixels):
        #threadVars = ThreadVariables(index, pixels)

        return threading.Thread(
                target=self.screenManager.drawScreen,
                args=(index, pixels))
