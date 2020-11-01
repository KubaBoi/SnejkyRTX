from SnejkyEngine.engine import Engine
from SnejkyEngine.objectManager import ObjectManager
from SnejkyEngine.vector import Vector
import math

class Object:
    def __init__(self, engine, position=(0,0,0)):
        self.engine = engine
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.radius = 10

    def getPosition(self):
        return Vector(self.x, self.y, self.z)

    def update(self):
        pass

    def draw(self):
        pass

    
    def isRayInRadius(self, ray):
        s1 = self.x
        s2 = self.y
        s3 = self.z

        c1 = self.engine.camera.position.x
        c2 = self.engine.camera.position.y
        c3 = self.engine.camera.position.z

        u1 = ray.direction[0]
        u2 = ray.direction[1]
        u3 = ray.direction[2]

        r = self.radius

        a = (- c1*c1*u2*u2 - c1*c1*u3*u3 + 2*c1*c2*u1*u2 + 2*c1*c3*u1*u3 + 2*c1*s1*u2*u2 + 2*c1*s1*u3*u3 - 2*c1*s2*u1*u2
         - 2*c1*s3*u1*u3 - c2*c2*u1*u1 - c2*c2*u3*u3 + 2*c2*c3*u2*u3 - 2*c2*s1*u1*u2 + 2*c2*s2*u1*u1 + 2*c2*s2*u3*u3 
         - 2*c2*s3*u2*u3 - c3*c3*u1*u1 - c3*c3*u2*u2 - 2*c3*s1*u1*u3 - 2*c3*s2*u2*u3 + 2*c3*s3*u1*u1 + 2*c3*s3*u2*u2 
         + r*r*u1*u1 + r*r*u2*u2 + r*r*u3*u3 - s1*s1*u2*u2 - s1*s1*u3*u3 + 2*s1*s2*u1*u2 + 2*s1*s3*u1*u3 - s2*s2*u1*u1 
         - s2*s2*u3*u3 + 2*s2*s3*u2*u3 - s3*s3*u1*u1 - s3*s3*u2*u2)

        b = (u1*u1 + u2*u2 + u3*u3)

        if (a < 0 or b == 0):
            return False
        return True

        """t = ((s1*u1 - c2*u2 - c3*u3 - c1*u1 + s2*u2 + s3*u3) - (c1*u1 + c2*u2 + c3*u3 - s1*u1 - s2*u2 - s3*u3) / b)

        x = c1 + t*u1
        y = c2 + t*u2
        z = c3 + t*u3
        print(x, y, z)
        d = math.sqrt(x*x + y*y + z*z)
        print(d)

        if (d <= self.radius):
            return True
        return False"""


