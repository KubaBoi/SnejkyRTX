import pygame

class Engine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.camera = "kamera"

    def update(self):
        