from SnejkyEngine.engine import Engine
from SnejkyEngine.objectManager import ObjectManager
from SnejkyEngine.object import Object
from SnejkyEngine.vector import Vector

class Light(Object):
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