from traceback import format_exc
import pygame
from pygame import surfarray
from pygame.locals import*
import time

from SnejkyEngine.engine import Engine
from SnejkyEngine.camera import Camera
from SnejkyEngine.vector import Vector
from SnejkyEngine.light import Light
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

    camera = Camera(Vector(0, 0, 0), Vector(0, 0, 1))

    engine = Engine(None, width, height, camera)

    #cervena
    koule = Ball(engine, 2, (0, 0, 50), (255, 20, 100))
    engine.addComponent(koule)
    #modra
    koule = Ball(engine, 2, (5, 2, -50), (0, 255, 255))
    engine.addComponent(koule)
    #zelena

    koule = Ball(engine, 2, (-10, 2, -45), (0, 255, 10))
    engine.addComponent(koule)

    light = Light(engine, (10, 0, -50))
    engine.lightManager.addLight(light)

    while running:
        tm = time.time()

        try:
            engine.update()
            running = False
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
