
class Tile():
    def __init__(self, testBoxX, testBoxY, image):
        self.testBoxX = testBoxX
        self.testBoxY = testBoxY
        self.image = image

class Floor(Tile):
    def __init__(self, testBoxX, testBoxY,image):
        super().__init__(testBoxX, testBoxY,image)

class Wall(Tile):
    def __init__(self, testBoxX, testBoxY,image):
        super().__init__(testBoxX, testBoxY,image)