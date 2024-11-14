import threading
from engine.lib import *

class Object:

    def __init__(self, pos: tuple):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.pos_z = pos[2]
        self.pos = pos

class Camera (Object):

    def __init__(self, pos: tuple[3], 
                 direction: tuple[3], 
                 screen_size: tuple[2]):
        """
        direction: vector, its size is screen's distance from camera
        screen_size: [width, height]
        """
        super(pos)
        self.direction = direction
        self.screen_size = screen_size

class Engine:

    def __init__(self):
        self.camera = Camera((0,0,0))
        self.Objects = []

    def draw_objects(self):
        for x in range(self.camera.screen_size[0]):
            for y in range(self.camera.screen_size[1]):
                pass

    

    
