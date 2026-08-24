from tkinter import *
import time
root = Tk()
root.geometry('800x800')
canvas = Canvas(root, bg='black', height=800, width=800)
canvas.pack()
column = 1
direction = 'left'
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
        canvas.move(self.square, 40, 0)
        self.x += 40
        self.d = 'left'
    def move_down(self):
        canvas.move(self.square, 0, 40)
        self.y += 40
        self.d = 'down'
    def move_right(self):
        canvas.move(self.square, -40, 0)
        self.x += -40
        self.d = 'right'
    def move_up(self):
        canvas.move(self.square, 0, -40)
        self.x += 40
        self.d = 'up'

class Snake:
    def __init__(self, length, x_coord, y_coord):
        self.length = length
        self.x = x_coord
        self.y = y_coord

root.mainloop()