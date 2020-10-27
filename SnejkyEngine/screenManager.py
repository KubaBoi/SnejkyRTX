import pygame
from pygame import surfarray
from pygame.locals import*
import numpy as np
import math
from multiprocessing import shared_memory, Process, Lock
from multiprocessing import cpu_count, current_process

from PIL import Image, ImageDraw

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

        self.pixelScreen = np.ndarray((self.width, self.height, 3), dtype=np.int64)  #dtype=np.uint8
        self.pixelScreen[0:self.width, 0:self.height] = (0,255,0)

    def updateScreen(self):
        pixelScreen = self.threadManager.update(self.width * self.height)
        #print(pixelScreen)
        pixelScreen = np.array(pixelScreen).reshape(self.width, self.height, 3)

        self.saveFrame(pixelScreen)
        #surfarray.blit_array(self.screen, pixelScreen)
        #pygame.display.flip()

    def drawScreen(self, index):
        x = index % self.width
        y = math.floor(index / self.width)
        oldPixel = self.pixelScreen[(x, y)]

        if (oldPixel[0] == 0 and oldPixel[1] == 255 and oldPixel[2] == 0):
            return (255, 0, 0)

        return (0, 0, 0)

    def saveFrame(self, pixelScreen):
        print("Saving frame...")

        img = Image.new("RGBA", (self.width, self.height), color=(0, 0, 0))
        pix = img.load()

        for y in range(self.height):
            for x in range(self.width):
                pix[x, y] = (pixelScreen[x, y][0], pixelScreen[x, y][1], pixelScreen[x, y][2]) 

        img.save("frame.png")
        print("Frame has been saved.")