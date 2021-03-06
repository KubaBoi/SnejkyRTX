from SnejkyEngine.vector import Vector

import math

class Ray:
    def __init__(self, engine, direction, startPoint, background=(200,200,200), level=0):
        self.engine = engine
        self.direction = direction
        self.color = (0,0,0)
        self.background = background
        self.level = level
        self.anyObject = False
        self.startPoint = startPoint

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def foundPixel(self):
        self.setColor(self.background)
        oldDistance = None

        for obj in self.engine.objectManager.objects:
            response = obj.isRayInRadius(self)
            if (response[0]):
                self.anyObject = True
                v = Vector(response[1].x - self.engine.camera.position.x,
                        response[1].y - self.engine.camera.position.y,
                        response[1].z - self.engine.camera.position.z)

                #pokud je objekt za kamerou
                if (v.angle(self.engine.camera.direction) > math.pi/2):
                    continue

                #poradi objektu v zavislosti na kamere
                distance = v.selfLength()
                if (oldDistance == None or oldDistance > distance): 
                    oldDistance = distance
                    
                    shadow = 0
                    #vypocteni stinu
                    if (self.level == 0):
                        light = self.engine.lightManager.lights[0]
                        shadowRay = Ray(self.engine, Vector(response[1].x - light.x,
                                                    response[1].y - light.y,
                                                    response[1].z - light.z),
                                                    response[1], self.background, self.level+1)
                        if (self.shootShadowRay(shadowRay, obj, light)): #true -> bude stin
                            shadow = 100
                        
                    self.setColor((obj.getColor()[0] - shadow, 
                                    obj.getColor()[1] - shadow,
                                    obj.getColor()[2] - shadow))

    def shootShadowRay(self, ray, objOld, light):
        for obj in self.engine.objectManager.objects:
            response = obj.inRadius(ray, objOld, light)
            
            #paprsek stinu narazil na objekt
            if (response):
                return True
        return False
