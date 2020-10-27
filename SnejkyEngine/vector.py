import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.position = (x, y, z)

    def selfLength(self):
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def distance(self, vector):
        return math.sqrt(pow(abs(self.x - vector.x), 2) + pow(abs(self.y - vector.y), 2) + pow(abs(self.z - vector.z), 2))