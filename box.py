from tkinter import *

class Game():
    def __init__(self):
        self.tiles = []

    def draw(self, canvas):
        canvas.create_rectangle(0, 0, 600, 600)
        for tile in self.tiles:
            canvas.create_image(tile.testBoxX, tile.testBoxY, anchor=NW, image = tile.image)
    
    def add_tiles(self, tiles):
        self.tiles.append(tiles)
        return self.tiles
    

class Tile():
    def __init__(self, testBoxX, testBoxY,image):
        self.testBoxX = testBoxX
        self.testBoxY = testBoxY
        self.image = image

class Floor(Tile):
    def __init__(self, testBoxX, testBoxY,image):
        super().__init__(testBoxX, testBoxY,image)

class Wall(Tile):
    def __init__(self, testBoxX, testBoxY,image):
        super().__init__(testBoxX, testBoxY,image)


   

    
    