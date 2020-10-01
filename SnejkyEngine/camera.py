class Camera:
    def __init__(self, position, direction):
        self.setCamera(position, direction)

    def setCamera(self, position, direction):
        self.position = position
        self.direction = direction