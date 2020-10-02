"""
testuje for cyklus pro vykresleni a rozdeleni programu do vlaken
"""

import pygame
import logging
import time
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from engine import Engine
from screenManager import ScreenManager

class DrawScreenTest:
    def __init__(self):
        width = 1920
        height = 1080
        screen = pygame.display.set_mode((width, height))
        self.ScreenManager = ScreenManager(Engine(screen, width, height, None))

    def test(self):
        self.ScreenManager.updateScreen()

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")

logging.info("Starting test for Drawing and Threading...")

try:
    t = time.time()
    test = DrawScreenTest()
    test.test()

    logging.info("-------------------")
    logging.info("Test done successfully")
except Exception as e:
    logging.info(e)
    logging.info("-------------------")
    logging.info("Test failed")
logging.info("Time: " + str(time.time() - t))