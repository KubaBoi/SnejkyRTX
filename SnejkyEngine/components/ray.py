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
                    
                    #vypocteni stinu
                    light = self.engine.lightManager.lights[0]
                    shadowRay = Ray(self.engine, Vector(light.x - response[1].x,
                                                light.y - response[1].y,
                                                light.z - response[1].z),
                                                response[1], self.background, self.level+1)

                    color = obj.getColor()
                    #self.calcPixelColor(obj, light, response[1])

                    shadow = self.shootShadowRay(shadowRay, obj, light) #stin
                    if (shadow == 0): #pokud pixel neni zastíněn, tak se vypočte jeho barva bez stinu
                        color = self.calcPixelColor(obj, light, response[1])
                        
                    self.setColor((color[0] - shadow, 
                                    color[1] - shadow,
                                    color[2] - shadow))

    def shootShadowRay(self, ray, objOld, light):
        for obj in self.engine.objectManager.objects:
            response = obj.isRayInRadius(ray, objOld, light)
            
            #paprsek stinu narazil na objekt
            if (response[0]):
                if (ray.startPoint.distance(light.getPosition()) >
                 response[1].distance(light.getPosition())):
                    return 200
        return 0

    #spocte zastineni pixelu v zavislosti na uhlu ke svetlu
    def calcPixelColor(self, obj, light, point):
        #uhel mezi vektorem (pixel - stred koule) a vektorem (pixel - svetlo)
        r = obj.getPosition().newVector(point)
        l = point.newVector(light.getPosition())

        multiplier = 2 #mozno pouzit jako nastaveni jasu
        angle = int((r.angle(l)*180 / math.pi)*multiplier)

        color = obj.getColor()
        color = (color[0] - angle,
                color[1] - angle,
                color[2] - angle)
        return color

