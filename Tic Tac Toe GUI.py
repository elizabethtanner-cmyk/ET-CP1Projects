from tkinter import *

root = Tk()
buttons = []
b = ['1', '2', '3', '4' ,'5', '6', '7', '8', '9'] #b for button values
turn = 1
l = ''

def press(i):
    global turn, b
    if turn %2 == 1:
        buttons[i].config(text='X', state='disabled')
        b[i] = 'x'
    else:
        buttons[i].config(text='O', state='disabled')
        b[i] = 'o'
    check_win()
def check_win():
    global b, l, turn, buttons
    print(b)
    if (b[0] == b[1] == b[2]) or (b[3] == b[4] == b[5]) or (b[6] == b[7] == b[8]) or (b[0] == b[3] == b[6]) or (b[1] == b[4] == b[7]) or (b[2] == b[5] == b[8]) or (b[0] == b[4] == b[8]) or (b[2] == b[4] == b[6]):
        if turn % 2 == 1:
            l = Label(root, text='X wins!', font = ('Courier', 50))
        else:
            l = Label(root, text='O wins!', font = ('Courier', 50))
        l.grid(row=3, columnspan=3)
        for i in buttons:
            i.config(state='disabled')
    for i in b:
        if i != 'x' and i != 'o':
            tie = False
            break
        tie = True
    if tie:
        l = Label(root, text='It\'s a Tie!', font = ('Courier', 50))
        l.grid(row=3, columnspan=3)
    turn += 1
    
for i in range(9):
    buttons.append(Button(root,font=('Courier', 50), width=3, height=1, command=lambda index=i: press(index)))
buttons[0].grid()
buttons[1].grid(row=0, column=1)
buttons[2].grid(row=0, column=2)
buttons[3].grid(row=1, column=0)
buttons[4].grid(row=1, column=1)
buttons[5].grid(row=1, column=2)
buttons[6].grid(row=2, column=0)
buttons[7].grid(row=2, column=1)
buttons[8].grid(row=2, column=2)



root.mainloop()