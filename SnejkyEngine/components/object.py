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

    
    def isRayInRadius(self, ray, obj=None, light=None):
        s1 = self.x
        s2 = self.y
        s3 = self.z

        c1 = ray.startPoint.x
        c2 = ray.startPoint.y
        c3 = ray.startPoint.z

        u1 = ray.direction.x
        u2 = ray.direction.y
        u3 = ray.direction.z

        r = self.radius

        #koeficienty rovnice
        A = u1*u1 + u2*u2 + u3*u3
        B = s1*u1 - c2*u2 - c3*u3 - c1*u1 + s2*u2 + s3*u3
        D = (- c1*c1*u2*u2
                - c1*c1*u3*u3
                + 2*c1*c2*u1*u2
                + 2*c1*c3*u1*u3
                + 2*c1*s1*u2*u2
                + 2*c1*s1*u3*u3
                - 2*c1*s2*u1*u2
                - 2*c1*s3*u1*u3
                - c2*c2*u1*u1
                - c2*c2*u3*u3
                + 2*c2*c3*u2*u3
                - 2*c2*s1*u1*u2
                + 2*c2*s2*u1*u1
                + 2*c2*s2*u3*u3
                - 2*c2*s3*u2*u3
                - c3*c3*u1*u1
                - c3*c3*u2*u2
                - 2*c3*s1*u1*u3
                - 2*c3*s2*u2*u3
                + 2*c3*s3*u1*u1
                + 2*c3*s3*u2*u2
                + r*r*u1*u1
                + r*r*u2*u2
                + r*r*u3*u3
                - s1*s1*u2*u2
                - s1*s1*u3*u3
                + 2*s1*s2*u1*u2
                + 2*s1*s3*u1*u3
                - s2*s2*u1*u1
                - s2*s2*u3*u3
                + 2*s2*s3*u2*u3
                - s3*s3*u1*u1
                - s3*s3*u2*u2)

        if (A == 0 or D < 0):
            return (False, Vector(0, 0, 0))
        elif (obj == self): #pokud se jedna o stejny objekt - stin je False
            return (False, Vector(0, 0, 0))

        t1 = (B + math.sqrt(D)) / (A)
        t2 = (B - math.sqrt(D)) / (A)

        #prusecik koule 1
        x1 = c1 + t1*u1 
        y1 = c2 + t1*u2
        z1 = c3 + t1*u3
        p1 = Vector(x1, y1, z1)

        #prusecik koule 2
        x2 = c1 + t2*u1
        y2 = c2 + t2*u2
        z2 = c3 + t2*u3
        p2 = Vector(x2, y2, z2)            

        #vybere blizsi prusecik
        if (p1.distance(ray.startPoint) > p2.distance(ray.startPoint)): #p2 je bliz
            return (True, p2)

        return (True, p1)