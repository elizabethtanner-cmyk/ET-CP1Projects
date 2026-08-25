from tkinter import *
import time
root = Tk()
root.geometry('800x800')
canvas = Canvas(root, bg='black', height=800, width=800)
canvas.pack()
column = 1
direction = 'right'
for i in range(20):
    line = canvas.create_line(column*40, 800, column*40, 0, fill='grey')
    column+= 1
row= 1
for i in range(20):
    line = canvas.create_line(0, row*40, 800, row*40, fill='grey')
    row += 1

class Body:
    
    def __init__(self, x, y, direction):
        self.d = direction
        self.square = canvas.create_polygon(x, y, x-38, y, x-38, y-38, x, y-38, fill='purple')
        self.x = x
        self.y = y 
    def move_left(self):
        canvas.move(self.square, -40, 0)
        self.x -= 40
        self.d = 'left'
    def move_down(self):
        canvas.move(self.square, 0, 40)
        self.y += 40
        self.d = 'down'
    def move_right(self):
        canvas.move(self.square, 40, 0)
        self.x += +40
        self.d = 'right'
    def move_up(self):
        canvas.move(self.square, 0, -40)
        self.y -= 40
        self.d = 'up'
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
class Snake:
    def __init__(self, length, x_coord, y_coord):
        self.length = length
        self.x = x_coord
        self.y = y_coord
        
b = Body(39, 39, direction)
b.move_right()

def change_left(e):
    global direction 
    direction = 'left'

def change_right(e):
    global direction 
    direction = 'right'

def change_down(e):
    global direction 
    direction = 'down'

def change_up(e):
    global direction 
    direction = 'up'

def end(e):
    exit()

def main():
    global direction 
    if direction == 'left':
        b.move_left()
    elif direction == 'right':
        b.move_right()
    elif direction == 'down':
        b.move_down()
    else:
        b.move_up()
    
    if (b.get_x() > 800) or (b.get_x() < 1) or (b.get_y() > 800) or (b.get_y() < 1):
        print('Game over!')
        exit()
    
    root.after(200, main)

root.bind('<Up>', change_up)
root.bind('w', change_up)
root.bind('<Down>', change_down)
root.bind('s', change_down)
root.bind('<Left>', change_left)
root.bind('a', change_left)
root.bind('<Right>', change_right)
root.bind('d', change_right)
root.bind('q', end)

main()

root.mainloop()