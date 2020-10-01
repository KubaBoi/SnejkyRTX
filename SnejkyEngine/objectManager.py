import pygame

class objectManager:
    def __init__(self):
        self.objects = []

    def updateObjects(self):
        for obj in self.objects:
            obj.update()

    def addObject(self, obj):
        self.objects.append(obj)

    def removeObject(self, obj):
        self.objects.remove(obj)