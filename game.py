from tkinter import *
import random
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
    





    
    