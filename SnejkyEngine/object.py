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

        u1 = ray.direction.x
        u2 = ray.direction.y
        u3 = ray.direction.z

        r = self.radius

        #koeficienty kvadraticky rovnice
        A = u1*u1 + u2*u2 + u3*u3
        B = 2*c1*u1 - 2*s1*u1 + 2*c2*u2 - 2*s2*u2 + 2*c3*u3 - 2*s3*u3 
        C = - 2*c1*s1 + s1*s1 - 2*c2*s2 + s2*s2 - 2*c3*s3 + s3*s3 - r*r

        #diskriminant
        D = B*B - 4*A*C

        if (A == 0 or D < 0):
            return (False, Vector(0, 0, 0))

        t1 = (-B + math.sqrt(D)) / 2*A
        t2 = (-B - math.sqrt(D)) / 2*A

        #prusecik koule 1
        x1 = c1 + t1*u1 
        y1 = c2 + t1*u2
        z1 = c3 + t1*u3

        #prusecik koule 2
        x2 = c1 + t2*u1
        y2 = c2 + t2*u2
        z2 = c3 + t2*u3

        if (c1 - x1 > c1 - x2 and
            c2 - y1 > c2 - y2 and
            c3 - z1 > c3 - z2):

            return (True, Vector(x2, y2, z2))

        return (True, Vector(x1, y1, z1))


    """
    metoda, kvuli stinu
    """
    def inRadius(self, ray, obj, light):
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

        #koeficienty kvadraticky rovnice
        A = u1*u1 + u2*u2 + u3*u3
        B = 2*c1*u1 - 2*s1*u1 + 2*c2*u2 - 2*s2*u2 + 2*c3*u3 - 2*s3*u3 
        C = - 2*c1*s1 + s1*s1 - 2*c2*s2 + s2*s2 - 2*c3*s3 + s3*s3 - r*r

        #diskriminant
        D = B*B - 4*A*C

        if (A == 0 or D < 0):
            return False
        elif (obj != self): #pokud se nejedna o stejny objekt - stin je True
            return True

        #objekt je stejny jako je v bode odrazu

        t1 = (-B + math.sqrt(D)) / 2*A
        t2 = (-B - math.sqrt(D)) / 2*A

        #prusecik koule 1
        x1 = c1 + t1*u1 
        y1 = c2 + t1*u2
        z1 = c3 + t1*u3

        #prusecik koule 2
        x2 = c1 + t2*u1
        y2 = c2 + t2*u2
        z2 = c3 + t2*u3

        #2 je bliz ke svetlu
        if (light.x - x1 > light.x - x2 and
            light.y - y1 > light.y - y2 and
            light.z - z1 > light.z - z2):

            #a pokud 2 je stejny jako bod odrazu
            if ((x2, y2, z2) == ray.startPoint.position):
                return False #potom na plose neni stin
            return True #jinak na plose je stin

        #1 je bliz k bodu odrazu
        #a pokud 1 je stejny jako bod odrazu
        if ((x1, y1, z1) == ray.startPoint.position):
            return False #potom na plose neni stin
        return True

