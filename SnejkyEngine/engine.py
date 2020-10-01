import pygame

from SnejkyEngine.objectManager import ObjectManager
from SnejkyEngine.lightManager import LightManager
from SnejkyEngine.screenManager import ScreenManager

class Engine:
    def __init__(self, screen, width, height, camera):
        self.width = width
        self.height = height
        self.camera = camera
        self.screen = screen

        self.objectManager = ObjectManager(self)
        self.lightManager = LightManager(self)
        self.screenManager = ScreenManager(self)

    def update(self):
        self.camera.update()
        self.objectManager.update()
        self.screenManager.updateScreen()

    def addComponent(self, Component):
        pass

    def removeComponent(self, Component):
        pass

    def setCamera(self, position, direction):
        self.camera.setCamera(position, direction)