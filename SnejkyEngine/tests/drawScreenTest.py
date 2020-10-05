"""
testuje for cyklus pro vykresleni a rozdeleni programu do vlaken
"""
if __name__ == "__main__":
    import pygame
    import logging
    import time
    import sys
    import os
    import multiprocessing
    from traceback import format_exc

    PACKAGE_PARENT = '..'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

    from engine import Engine
    from screenManager import ScreenManager

    class DrawScreenTest:
        def __init__(self):
            width = 10
            height = 10
            #screen = pygame.display.set_mode((width, height))
            self.ScreenManager = ScreenManager(Engine(None, width, height, None))

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
        print(repr(e))
        print(format_exc())
        logging.info("-------------------")
        logging.info("Test failed")
    logging.info("Time: " + str(time.time() - t))