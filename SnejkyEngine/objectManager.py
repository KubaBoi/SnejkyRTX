class ObjectManager:
    def __init__(self, engine):
        self.objects = []
        self.engine = engine

    def update(self):
        for obj in self.objects:
            obj.update()

    def addObject(self, obj):
        self.objects.append(obj)

    def removeObject(self, obj):
        self.objects.remove(obj)