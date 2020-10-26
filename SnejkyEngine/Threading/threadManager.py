import math
from multiprocessing import shared_memory, Process, Lock, Pool
from multiprocessing import cpu_count, current_process
import numpy as np
import time
import os
import sys

try:
    from SnejkyEngine.Threading.threadVariables import ThreadVariables
except: #testing

    PACKAGE_PARENT = '..'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
    from Threading.threadVariables import ThreadVariables

class ThreadManager:
    def __init__(self, screenManager):
        self.screenManager = screenManager
        self.threadCount = cpu_count()-1


    def update(self, countOfPixels):
        with Pool(processes=self.threadCount) as pool:
            pixelScreen = pool.map(self.screenManager.drawScreen, range(countOfPixels))

            return pixelScreen
