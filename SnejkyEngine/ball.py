from SnejkyEngine.engine import Engine
from SnejkyEngine.object import Object
from SnejkyEngine.objectManager import ObjectManager
from SnejkyEngine.vector import Vector

class Ball(Object):
    def __init__(self, engine, radius, position=(0,0,0), color=(255,0,0)):
        Object.__init__(self, engine, position)
        self.engine = engine
        self.radius = radius
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.color = color

    def getPosition(self):
        return Vector(self.x, self.y, self.z)

    def update(self):
        pass

    def getColor(self):
        return self.color