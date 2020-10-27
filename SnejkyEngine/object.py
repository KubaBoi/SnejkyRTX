from engine import Engine
from objectManager import ObjectManager

class Object:
    def __init__(self, engine, position=(0,0,0)):
        self.engine = engine
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]

    def update(self):
        pass

    def draw(self):
        pass 