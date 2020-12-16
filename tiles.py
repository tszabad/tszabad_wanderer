
class Tile():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

class Floor(Tile):
    def __init__(self, x, y,image):
        super().__init__(x, y,image)

class Wall(Tile):
    def __init__(self, x, y,image):
        super().__init__(x, y,image)