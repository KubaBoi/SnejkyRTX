from traceback import format_exc
import time
import math

from SnejkyEngine.engine import Engine
from SnejkyEngine.camera import Camera
from SnejkyEngine.vector import Vector
from SnejkyEngine.light import Light
from SnejkyEngine.ball import Ball

if __name__ == "__main__":
    width = 800
    height = 800

    running = True


    camera = Camera(Vector(0, 0, 0), Vector(0, 0, -1))

    engine = Engine(None, width, height, camera)

    #cervena
    koule = Ball(engine, 2, (0, 0, -50), (255, 20, 100))
    engine.addComponent(koule)
    #velka modra
    koule = Ball(engine, 10, (0, -15, -50), (0, 255, 255))
    engine.addComponent(koule)
    #modra
    koule = Ball(engine, 2, (10, 2, -50), (0, 255, 255))
    engine.addComponent(koule)
    #zelena
    koule = Ball(engine, 2, (-10, 2, -45), (0, 255, 10))
    engine.addComponent(koule)

    light = Light(engine, (0, 10, -50))
    engine.lightManager.addLight(light)

    i = 0
    while running:
        tm = time.time()

        try:
            #engine.lightManager.lights[0].y = math.sin(i*math.pi/180)*50
            #engine.lightManager.lights[0].z = math.sin(i*math.pi/180)*-50
            engine.update()
            if (i >= 0):
                running = False
            i += 1
        except Exception as e:
            print(repr(e))
            print(format_exc())
            running = False

        l = time.time()-tm
        print(l)
