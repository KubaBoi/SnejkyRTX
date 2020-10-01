import pygame
import numpy as np
import math

from SnejkyEngine.threadManager import ThreadManager

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

    def drawScreen(self, threadIndex, numberOfPixels):
        pass