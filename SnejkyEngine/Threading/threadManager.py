import math
import multiprocessing

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
        self.threadCount = multiprocessing.cpu_count()-1


    def update(self, countOfPixels):
        oneThreadPixels = math.floor(countOfPixels/self.threadCount)

        pic = []
        finalScreen = multiprocessing.Array(self.screenManager.pixelScreen, 10)

        threads = []
        for i in range(0, self.threadCount):
            if (i < self.threadCount):
                x = self.createThread(i+1, oneThreadPixels, finalScreen)
            else:
                x = self.createThread(self.threadCount, 
                        countOfPixels - (oneThreadPixels * (self.threadCount-1)), finalScreen)
            threads.append(x)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        print(finalScreen)

    def createThread(self, index, pixels, queue):
        return multiprocessing.Process(
                target=self.screenManager.drawScreen,
                args=(index, pixels, queue))
