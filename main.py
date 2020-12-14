from tkinter import *

from game import Game
from tiles import Floor, Wall
from characters import Hero, Skeleton, Boss
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
    skeleton = PhotoImage(file="images/skeleton.png")
    boss = PhotoImage(file="images/boss.png")
    
    #instasiating objects
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

    skelet = Skeleton(9,7,skeleton)
    skelet2 = Skeleton(0,9, skeleton)
    skelet3 = Skeleton(6,0, skeleton)
    skelets = [skelet, skelet2, skelet3]
    hero = Hero(0,0,hero_down)       
    boss = Boss(6,3,boss)

#  function that can be called when a key pressing happens
    def on_key_press(e):
        def coords(char):
            x, y = char.get_coordinates()
            x, y = int(x/60), int(y/60)
            return x, y
        if e.keycode == 83 and m.matrix[coords(hero)[1]+1][coords(hero)[0]] != 1 and coords(hero)[1]<=9:  #down
            hero.set_coordinatesY(60)
            hero.set_image(hero_down)
        elif e.keycode == 87 and m.matrix[coords(hero)[1]-1][coords(hero)[0]] != 1 and coords(hero)[1]>0:   #up
            hero.set_coordinatesY(-60)
            hero.set_image(hero_up)
        elif e.keycode == 65 and m.matrix[coords(hero)[1]][coords(hero)[0]-1] != 1 and coords(hero)[0]>0:     #left
            hero.set_coordinatesX(-60)
            hero.set_image(hero_left)
        elif e.keycode == 68 and m.matrix[coords(hero)[1]][coords(hero)[0]+1] != 1 and coords(hero)[0]<=9:   #right
            hero.set_coordinatesX(60)
            hero.set_image(hero_right)
        elif e.keycode == 27:                #exit
            root.destroy()
        elif e.keycode == 32 and coords(hero) == coords(boss):
            hero.battle(boss)
        elif e.keycode == 32 and coords(hero) == coords(skelet):
            hero.battle(skelet)
        elif e.keycode == 32 and coords(hero) == coords(skelet2):
            hero.battle(skelet2)
        elif e.keycode == 32 and coords(hero) == coords(skelet3):
            hero.battle(skelet3)


        stats()
        draw_canvas()
        
# Tell the canvas that we prepared a function that can deal with the key press events
    canvas.bind("<KeyPress>", on_key_press)
    canvas.pack()

# Select the canvas to be in focused so it actually recieves the key hittings
    canvas.focus_set()
    def draw_canvas():
        game.draw(canvas)
        hero.draw_character(canvas)
        for skel in skelets:
            skel.draw_character(canvas)
        boss.draw_character(canvas)
    draw_canvas()
    
    #game stats
    canvas2 = Canvas(root, width=600, height=30)
    def stats():
        canvas2.create_rectangle(0, 0, 600, 30, fill = "grey")
        text = f"Hero (Level: {hero.level}) HP: {hero.HP}/38 | DP: {hero.DP} | SP: {hero.SP}"
        canvas_text = canvas2.create_text(10, 10, text=text, font=('freemono bold',11),anchor=NW)
        canvas2.pack()

    root.mainloop()


if __name__ == '__main__':
    main()