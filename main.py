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
        def coords():
            x, y = hero.get_coordinates()
            x, y = int(x/60), int(y/60)
            return x, y

        if e.keycode == 83 and m.matrix[coords()[1]+1][coords()[0]] != 1 and coords()[1]<=9:  #down
            hero.set_coordinatesY(60)
            hero.set_image(hero_down)
            
        elif e.keycode == 87 and m.matrix[coords()[1]-1][coords()[0]] != 1 and coords()[1]>0:   #up
            hero.set_coordinatesY(-60)
            hero.set_image(hero_up)
            
        elif e.keycode == 65 and m.matrix[coords()[1]][coords()[0]-1] != 1 and coords()[0]>0:     #left
            hero.set_coordinatesX(-60)
            hero.set_image(hero_left)
            
        elif e.keycode == 68 and m.matrix[coords()[1]][coords()[0]+1] != 1 and coords()[0]<=9:   #right
            hero.set_coordinatesX(60)
            hero.set_image(hero_right)
        
        game.draw(canvas)
        hero.draw(canvas)
        coords()
        

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