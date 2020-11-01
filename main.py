from traceback import format_exc
import pygame
from pygame import surfarray
from pygame.locals import*
import time

from SnejkyEngine.engine import Engine
from SnejkyEngine.camera import Camera
from SnejkyEngine.vector import Vector
from SnejkyEngine.ball import Ball

if __name__ == "__main__":

    #pygame.init()

    #full screen
    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    width = 800
    height = 800
    #screen = pygame.display.set_mode((width, height))

    color = (255, 255, 255)
    #screen.fill((color))
    running = True

    #clock = pygame.time.Clock()

    camera = Camera(Vector(0, 0, 0), Vector(0, 0, -1))

    engine = Engine(None, width, height, camera)

    koule = Ball(engine, 20, (0, 0, -100))
    engine.addComponent(koule)

    while running:
        tm = time.time()

        try:
            engine.update()
        except Exception as e:
            print(repr(e))
            print(format_exc())
            running = False
        
        """for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False"""

        l = time.time()-tm
        print(l)

    #pygame.quit()
