from tkinter import *

from game import Game, Floor, Wall, Hero
import matrix as m
      
def main():
    root = Tk()
    root.title("Tom's wanderer game")
    canvas = Canvas(root, width=600, height=600)

    floor = PhotoImage(file="images/floor.png")
    wall = PhotoImage(file="images/wall.png")
    hero_down = PhotoImage(file="images/hero-down.png")
    hero_up = PhotoImage(file="images/hero-up.png")
    hero_left = PhotoImage(file="images/hero-left.png")
    hero_right = PhotoImage(file="images/hero-right.png")
    
    game = Game()

    for i in range(0,10):
        if m.matrix[0][i] == 0:
            tile = Floor(i*60,0, floor)
            game.add_tiles(tile)
        else:
             tile = Wall(i*60,0, wall)
             game.add_tiles(tile)
        for j in range(1,10):
            if m.matrix[j][i] == 0:
                tile = Floor(i*60,j*60, floor)
                game.add_tiles(tile)
            else:
                tile = Wall(i*60,j*60, wall)
                game.add_tiles(tile)
    
    hero = Hero(0,0,hero_down) 
# Create a function that can be called when a key pressing happens
    def on_key_press(e):
        if e.keycode == 83:  #down
            hero.set_coordinatesY(60)
            hero.set_image(hero_down)
        elif e.keycode == 87:   #up
            hero.set_coordinatesY(-60)
            hero.set_image(hero_up)
        elif e.keycode == 65:     #left
            hero.set_coordinatesX(-60)
            hero.set_image(hero_left)
        elif e.keycode == 68:   #right
            hero.set_coordinatesX(60)
            hero.set_image(hero_right)
        game.draw(canvas)
        hero.draw(canvas)

# Tell the canvas that we prepared a function that can deal with the key press events
    canvas.bind("<KeyPress>", on_key_press)
    canvas.pack()

# Select the canvas to be in focused so it actually recieves the key hittings
    canvas.focus_set()
    game.draw(canvas)
    hero.draw(canvas)

    root.mainloop()


if __name__ == '__main__':
    main()