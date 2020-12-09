from tkinter import *

from box import Box
      

root = Tk()
canvas = Canvas(root, width=600, height=600)

floor = PhotoImage(file="images/floor.png")
box = Box(0,0,floor)
box2 = Box(0,61, floor)

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
box.draw(canvas)
box2.draw(canvas)

root.mainloop()

