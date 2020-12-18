import random
from tkinter import *

class Hero():
    def __init__(self, x, y, image):
        self.x = x *60
        self.y = y *60
        self.image = image
        self.HP = 20 + 3 * random.randint(1,6)
        self.maxHP = 38
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
    
    def set_level(self, level):
        self.level = level

    def increase_HP(self, hp):
        self.HP += hp

    def set_HP(self, hp):
        self.HP = hp
        
    def strike(self, opponent):
        if isinstance(self, Hero):
            SV = self.SP + random.randint(1,6)
            if ((2 * random.randint(1,6)) + SV) > opponent.DP:
                opponent.HP -= SV-opponent.DP
        else:
            SV = opponent.SV + random.randint(1,6)
            if ((2 * random.randint(1,6)) + SV) > self.DP:
                self.HP -= SV-self.DP

    def battle(self, opponent):
        if self.HP and opponent.HP > 0:
            self.strike(opponent)
            opponent.strike(self)
        else:
            if isinstance(self, Hero) and opponent.HP < self.HP:
                self.maxHP += random.randint(1,6)
                self.DP += random.randint(1,6)
                self.SP += random.randint(1,6)
                return opponent
            else:
                print("hero died")   
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
      