import pygame

try:
    from SnejkyEngine.objectManager import ObjectManager
    from SnejkyEngine.lightManager import LightManager
    from SnejkyEngine.screenManager import ScreenManager
except: #testing
    import sys
    import os

    PACKAGE_PARENT = '..'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
    from objectManager import ObjectManager
    from lightManager import LightManager
    from screenManager import ScreenManager

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