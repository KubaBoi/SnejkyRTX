class lightManager:
    def __init__(self, engine):
        self.lights = []
        self.engine = engine

    def addLight(self, light):
        light.setEngine(self.engine)
        self.lights.append(light)

    def removeLight(self, light):
        self.lights.remove(light)