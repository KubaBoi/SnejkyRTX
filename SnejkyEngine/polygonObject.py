from engine import Engine
from object import Object
from objectManager import ObjectManager
from vector import Vector

class PlaygonObjectObject(Object):
    def __init__(self, engine, position=(0,0,0)):
        Object.__init__(self, engine, position)
        self.engine = engine
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]

    def getPosition(self):
        return Vector(self.x, self.y, self.z)

    def update(self):
        pass

    def draw(self):
        pass 