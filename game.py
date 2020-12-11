from tkinter import *
import random


class Game():
    def __init__(self):
        self.tiles = []
        self.character = []

    def draw(self, canvas):
        canvas.create_rectangle(0, 0, 600, 600)
        for tile in self.tiles:
            canvas.create_image(tile.testBoxX, tile.testBoxY, anchor=NW, image = tile.image)
    
    def add_tiles(self, tiles):
        self.tiles.append(tiles)
        return self.tiles
    

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

class Hero():
    def __init__(self, x, y, image):
        self.x = x *60
        self.y = y *60
        self.image = image
        self.HP = 20 + 3 * random.randint(1,6)
        self.DP = 2 * random.randint(1,6)
        self.SP = 5 + random.randint(1,6)

    def draw_character(self, canvas):
        canvas.create_image(self.x, self.y, anchor=NW, image = self.image)
        
   
    def get_coordinates(self):
        return self.x, self.y

    def set_coordinatesX(self, x):
        self.x += x

    def set_coordinatesY(self, y):
        self.y += y
       
    def set_image(self, image):
        self.image = image
class Skeleton(Hero):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
      
class Boss(Hero):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
      

    
    