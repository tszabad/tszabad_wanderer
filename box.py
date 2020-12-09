from tkinter import *

class Box(object):
    def __init__(self, testBoxX, testBoxY,image):
        self.testBoxX = testBoxX
        self.testBoxY = testBoxY
        self.image = image

    def draw(self, canvas):
        canvas.create_rectangle(0, 0, 600, 600)
        
        canvas.create_image(self.testBoxX, self.testBoxY, anchor=NW, image = self.image)
        