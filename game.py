from tkinter import *
import random

from tiles import Floor, Wall
from characters import Hero, Boss, Skeleton
import matrix as m

class Game():
    def __init__(self, hero):
        self.hero = hero
        self.tiles = []
        floor = PhotoImage(file="images/floor.png")
        wall = PhotoImage(file="images/wall.png")
        skeleton = PhotoImage(file="images/skeleton.png")
        boss = PhotoImage(file="images/boss.png")

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

        skelet = Skeleton(9,7,skeleton)
        skelet2 = Skeleton(0,9, skeleton)
        skelet3 = Skeleton(6,0, skeleton)
        boss = Boss(6,3,boss)
        self.characters = [skelet, skelet2, skelet3, boss]

    def draw(self, canvas):
        canvas.create_rectangle(0, 0, 600, 600)
        for tile in self.tiles:
            canvas.create_image(tile.x, tile.y, anchor=NW, image = tile.image)
    
    def add_tiles(self, tiles):
        self.tiles.append(tiles)
        return self.tiles

    def draw_character(self,canvas):
        for char in self.characters:
            canvas.create_image(char.x, char.y, anchor=NW, image = char.image)

    def remove_character(self, character):
        self.characters.remove(character)

    def get_characters(self):
        return self.characters


    
    
    





    
    