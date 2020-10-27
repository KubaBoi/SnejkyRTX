"""
testuje for cyklus pro vykresleni a rozdeleni programu do vlaken
"""

import pygame
import sys
import os
from test import Test

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from engine import Engine
from screenManager import ScreenManager

class DrawScreenTest(Test):
        def __init__(self):
            self.name = "Drawing and Threading"
            Test.__init__(self, self.name)

        def doTest(self):
            return Test.doTest(self, self)

        def test(self):
            width = 1920
            height = 1080

            screen = None#pygame.display.set_mode((width, height))
            #screen = pygame.display.set_mode((width, height))
            self.ScreenManager = ScreenManager(Engine(screen, width, height, None))

            self.ScreenManager.updateScreen()
            return True