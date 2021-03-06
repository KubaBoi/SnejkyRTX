class LightManager:
    def __init__(self, engine):
        self.lights = []
        self.engine = engine

    def addLight(self, light):
        self.lights.append(light)

    def removeLight(self, light):
        self.lights.remove(light)