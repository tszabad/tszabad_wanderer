from tkinter import *

from game import Game
from characters import Hero, Skeleton, Boss
import matrix as m
      
def main():
    root = Tk()
    root.title("Tom's wanderer game")
    canvas = Canvas(root, width=600, height=600)

    # importing pictures
    hero_down = PhotoImage(file="images/hero-down.png")
    hero_up = PhotoImage(file="images/hero-up.png")
    hero_left = PhotoImage(file="images/hero-left.png")
    hero_right = PhotoImage(file="images/hero-right.png")
    
    
    #instasiating objects
    
    hero = Hero(0,0,hero_down)
    game = Game(hero)

    def new_level(game):
        if len(game.characters) == 0:
            game = Game(hero)
            print(game)
            hero.level_up()
        else:
            game = game
        return game
    print(game)
    
    

#  function that can be called when a key pressing happens
    def on_key_press(e):
        def coords(char):
            x, y = char.get_coordinates()
            x, y = int(x/60), int(y/60)
            return x, y
        try:
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
        except(IndexError):
            pass
         #exit
        if e.keycode == 27:               
            root.destroy()
        #battle
        opponent = False
        for char in game.get_characters():
            if e.keycode == 32 and coords(hero) == coords(char):
                opponent = hero.battle(char)
                if opponent:
                    game.remove_character(opponent)
                    new_level(game)
                  
               
        canvas.delete("all")
        stats()    
        draw_canvas()
        
        
# binding key press events
    canvas.bind("<KeyPress>", on_key_press)
    canvas.pack()
        
    
# draw the canvas
    def draw_canvas():
        game.draw(canvas)
        game.draw_character(canvas)
        hero.draw_character(canvas)
    draw_canvas()
    canvas.focus_set()
#game stats
    canvas2 = Canvas(root, width=600, height=30)
    def stats():
        canvas2.create_rectangle(0, 0, 600, 30, fill = "grey")
        text = f"Hero (Level: {hero.level}) HP: {int(hero.HP)}/38 | DP: {hero.DP} | SP: {hero.SP}"
        canvas_text = canvas2.create_text(10, 10, text=text, font=('freemono bold',11),anchor=NW)
        canvas2.pack()

    root.mainloop()


if __name__ == '__main__':
    main()