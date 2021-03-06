import pygame
from pygame import surfarray
from pygame.locals import*
import numpy as np
import math
from multiprocessing import shared_memory, Process, Lock
from multiprocessing import cpu_count, current_process
from traceback import format_exc

from PIL import Image, ImageDraw

try:
    from SnejkyEngine.Threading.threadManager import ThreadManager
    from SnejkyEngine.Threading.threadVariables import ThreadVariables
    from SnejkyEngine.vector import Vector
    from SnejkyEngine.ray import Ray
except Exception as e: #testing
    print(repr(e))
    print(format_exc())
    import sys
    import os

    PACKAGE_PARENT = '..'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
    from Threading.threadManager import ThreadManager
    from Threading.threadVariables import ThreadVariables
    from vector import Vector
    from ray import Ray

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
        #pixelScreen = self.threadManager.update(self.width * self.height)
        #pixelScreen = np.array(pixelScreen).reshape(self.height, self.width, 3)

        pixelScreen = []
        for i in range(self.width * self.height):
            pixelScreen.append(self.drawScreen(i))

        pixelScreen = self.reshape(pixelScreen)

        self.saveFrame(pixelScreen)

    def drawScreen(self, index):
        x = index % self.width
        y = math.floor(index / self.width)
        oldPixel = self.pixelScreen[(x, y)]

        if (oldPixel[0] == 0 and oldPixel[1] == 255 and oldPixel[2] == 0):
            ray = Ray(self.engine, 
                Vector(round(x - self.width / 2), round(y - self.height / 2), -1000),
                self.engine.camera.position)

            ray.foundPixel()
            return ray.getColor()

        return (0, 0, 0)

    def saveFrame(self, pixelScreen):
        print("Saving frame...")

        img = Image.new("RGBA", (self.width, self.height), color=(0, 0, 0))
        pix = img.load()

        for y in range(1, self.height+1):
            for x in range(self.width):
                pix[x, y-1] = (pixelScreen[self.height-y][x][0],
                            pixelScreen[self.height-y][x][1], 
                            pixelScreen[self.height-y][x][2])

        img.save("frame.png")
        print("Frame has been saved.")

    def reshape(self, pixelScreen):
        pix = []
        for y in range(self.height):
            pix.append([])
            for x in range(self.width):
                pix[y].append(pixelScreen[y*self.width + x])

        return pix