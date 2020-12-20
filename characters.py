from tkinter import *

from utils import Utils

class Hero():
    def __init__(self, x, y, image):
        self.x = x *60
        self.y = y *60
        self.image = image
        self.HP = 20 + 3 * Utils.get_random()
        self.maxHP = 38
        self.DP = 2 * Utils.get_random()
        self.SP = 5 + Utils.get_random()
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
            SV = self.SP + Utils.get_random()
            if ((2 * Utils.get_random()) + SV) > opponent.DP:
                opponent.HP -= SV-opponent.DP
        else:
            SV = opponent.SV + Utils.get_random()
            if ((2 * Utils.get_random()) + SV) > self.DP:
                self.HP -= SV-self.DP

    def battle(self, opponent):
        if self.HP and opponent.HP > 0:
            self.strike(opponent)
            opponent.strike(self)
        else:
            if isinstance(self, Hero) and opponent.HP < self.HP:
                self.maxHP += Utils.get_random()
                self.DP += Utils.get_random()
                self.SP += Utils.get_random()
                return opponent
            else:
                print("hero died")   
class Skeleton(Hero):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.HP = 2 * self.level * Utils.get_random()
        self.DP = self.level / 2 * Utils.get_random()
        self.SP = self.level * Utils.get_random()
class Boss(Hero):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.HP = 2 * self.level * Utils.get_random() + Utils.get_random()
        self.DP = self.level / 2 * Utils.get_random() +Utils.get_random()/2
        self.SP = self.level * Utils.get_random() + self.level
      