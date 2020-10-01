import math
import threading

class ThreadManager:
    def __init__(self, screenManager):
        self.screenManager = screenManager
        self.threadCount = 4

    def update(self, countOfPixels):
        oneThreadPixels = math.floor(countOfPixels/self.threadCount)

        threads = []
        for i in range(1, self.threadCount):
            x = self.createThread(i, oneThreadPixels)
            threads.append(x)
            x.start()

        #prida se posledni vlakno
        x = self.createThread(self.createThread, 
                        countOfPixels - (oneThreadPixels * (self.threadCount-1)))
        threads.append(x)
        x.start()

        for index, thread in enumerate(threads):
            thread.join()

    def createThread(self, index, pixels):
        return threading.Thread(
                target=self.screenManager.drawScreen,
                args=(index, pixels))