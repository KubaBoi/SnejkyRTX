import pygame
from pygame import surfarray
from pygame.locals import*
import numpy as np
import math

try:
    from SnejkyEngine.Threading.threadManager import ThreadManager
    from SnejkyEngine.Threading.threadVariables import ThreadVariables
except: #testing
    import sys
    import os

    PACKAGE_PARENT = '..'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
    from Threading.threadManager import ThreadManager
    from Threading.threadVariables import ThreadVariables

class ScreenManager:
    def __init__(self, engine):
        self.engine = engine
        self.threadManager = ThreadManager(self)
        self.screen = engine.screen
        
        self.width = engine.width
        self.height = engine.height

        self.pixelScreen = np.zeros((self.width, self.height, 3), dtype=np.uint8)    
        self.pixelScreen[0:self.width, 0:self.height] =  (255,255,255)

    def updateScreen(self):
        self.threadManager.update(self.width * self.height)

        surfarray.blit_array(self.screen, self.pixelScreen)
        pygame.display.flip()

    def drawScreen(self, index, pixels):
        threadVars = ThreadVariables(index, pixels)
        startingIndex = (threadVars.index - 1) * threadVars.numberOfPixels
        a = 0
        for i in range(0, threadVars.numberOfPixels):
            startingIndex += 1
            for x in range(0, 50):
                a += 1

        print("\n" + str(threadVars.index) + ": " + str(threadVars.numberOfPixels) + " - " + str(startingIndex) + "\n")