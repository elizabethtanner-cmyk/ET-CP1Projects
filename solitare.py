from tkinter import *
import random
root = Tk()
root.geometry('900x900')
canvas = Canvas(root, height=900, width=900, bg='green')
canvas.pack()

cards = ['A Spades', '2 Spades', '3 Spades', '4 Spades', '5 Spades', '6 Spades', '7 Spades', '8 Spades', '9 Spades', '10 Spades', 'J Spades', 'Q Spades', 'K Spades', \
         'A Hearts', '2 Hearts', '3 Hearts', '4 Hearts', '5 Hearts', '6 Hearts', '7 Hearts', '8 Hearts', '9 Hearts', '10 Hearts', 'J Hearts', 'Q Hearts', 'K Hearts', \
         'A Clubs', '2 Clubs', '3 Clubs', '4 Clubs', '5 Clubs', '6 Clubs', '7 Clubs', '8 Clubs', '9 Clubs', '10 Clubs', 'J Clubs', 'Q Clubs', 'K Clubs', \
         'A Diamonds', '2 Diamonds', '3 Diamonds', '4 Diamonds', '5 Diamonds', '6 Diamonds', '7 Diamonds', '8 Diamonds', '9 Diamonds', '10 Diamonds', 'J Diamonds', 'Q Diamonds', 'K Diamonds']
shuffled = []
card = ''
for i in range(len(cards)):
    while card in shuffled:
        card = random.choice(cards)
    if i == 0:
        card = random.choice(cards)
    shuffled.append(card)


    


root.mainloop()

