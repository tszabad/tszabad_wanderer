from tkinter import *
import random

from tiles import Floor, Wall
import matrix as m

class Game():
    def __init__(self):
        self.tiles = []
        floor = PhotoImage(file="images/floor.png")
        wall = PhotoImage(file="images/wall.png")

        for i in range(0,10):
            if m.matrix[0][i] == 0:
                tile = Floor(i*60,0, floor)
                self.add_tiles(tile)
            else:
                tile = Wall(i*60,0, wall)
                self.add_tiles(tile)
            for j in range(1,10):
                if m.matrix[j][i] == 0:
                    tile = Floor(i*60,j*60, floor)
                    self.add_tiles(tile)
                else:
                    tile = Wall(i*60,j*60, wall)
                    self.add_tiles(tile)

    def draw(self, canvas):
        canvas.create_rectangle(0, 0, 600, 600)
        for tile in self.tiles:
            canvas.create_image(tile.testBoxX, tile.testBoxY, anchor=NW, image = tile.image)
    
    def add_tiles(self, tiles):
        self.tiles.append(tiles)
        return self.tiles
    





    
    