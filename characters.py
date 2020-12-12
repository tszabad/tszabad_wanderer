import random
from tkinter import *

class Hero():
    def __init__(self, x, y, image):
        self.x = x *60
        self.y = y *60
        self.image = image
        self.HP = 20 + 3 * random.randint(1,6)
        self.DP = 2 * random.randint(1,6)
        self.SP = 5 + random.randint(1,6)
        self.level = 1

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

    def level_up(self):
        self.level += 1

    def strike(self, monster):
        pass


class Skeleton(Hero):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.HP = 2 * self.level * random.randint(1,6)
        self.DP = self.level / 2 * random.randint(1,6)
        self.SP = self.level * random.randint(1,6)
      
class Boss(Hero):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.HP = 2 * self.level * random.randint(1,6) + random.randint(1,6)
        self.DP = self.level / 2 * random.randint(1,6) +random.randint(1,6)/2
        self.SP = self.level * random.randint(1,6) + self.level
      