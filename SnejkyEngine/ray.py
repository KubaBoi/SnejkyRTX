from SnejkyEngine.vector import Vector

class Ray:
    def __init__(self, engine, direction, background=(200,200,200)):
        self.engine = engine
        self.direction = direction
        self.color = (0,0,0)
        self.background = background

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def foundPixel(self):
        self.setColor(self.background)

        for object in self.engine.objectManager.objects:
            if (object.isRayInRadius(self)):
                self.setColor(object.getColor())