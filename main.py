from traceback import format_exc
import pygame
from pygame import surfarray
from pygame.locals import*
import time

from SnejkyEngine.engine import Engine
from SnejkyEngine.screen import Screen

pygame.init()

#full screen
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

color = (255, 255, 255)
screen.fill((color))
running = True

clock = pygame.time.Clock()

engine = Engine()

while running:
    tm = time.time()
    
    try:
        engine.Update()
        engine.Draw()
    except Exception as e:
        print(repr(e))
        print(format_exc())
        running = False

    sc.createScreen(screen)
    #surfarray.blit_array(screen, sc.drawScreen())
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    l = time.time()-tm
    #print(l)

pygame.quit()
