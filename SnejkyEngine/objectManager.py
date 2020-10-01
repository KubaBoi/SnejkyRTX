class objectManager:
    def __init__(self, engine):
        self.objects = []
        self.engine = engine

    def updateObjects(self):
        for obj in self.objects:
            obj.update()

    def addObject(self, obj):
        obj.setEngine(self.engine)
        self.objects.append(obj)

    def removeObject(self, obj):
        self.objects.remove(obj)