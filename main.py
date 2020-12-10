from tkinter import *

from box import Game, Floor
      
def main():
    root = Tk()
    canvas = Canvas(root, width=600, height=600)
    floor = PhotoImage(file="images/floor.png")
    
    game = Game()

    for i in range(0,10):
        tile = Floor(i*60,0, floor)
        game.add_tiles(tile)
        for j in range(1,10):
            tile = Floor(i*60,j*60, floor)
            game.add_tiles(tile)
            print(tile)
       
    
        

# Create a function that can be called when a key pressing happens
    def on_key_press(e):
        # When the keycode is 111 (up arrow) we move the position of our box higher
        if e.keycode == 111:
            box.testBoxY = box.testBoxY - 100
        elif e.keycode == 116:
            box.testBoxY = box.testBoxY + 100
    # and lower if the key that was pressed the down arrow
    # draw the box again in the new position
        box.draw(canvas)

# Tell the canvas that we prepared a function that can deal with the key press events
    canvas.bind("<KeyPress>", on_key_press)
    canvas.pack()

# Select the canvas to be in focused so it actually recieves the key hittings
    canvas.focus_set()

# Draw the box in the initial position
    for tile in game.tiles:
        game.draw(canvas)
    

    root.mainloop()



if __name__ == '__main__':
    main()