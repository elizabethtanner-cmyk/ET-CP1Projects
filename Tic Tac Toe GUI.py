from tkinter import *
root = Tk()
color = 'black'
root.title('Tic Tac Toe!!!')
root.config(bg=color)
buttons = []
b = ['1', '2', '3', '4' ,'5', '6', '7', '8', '9'] #b for button values
turn = 1


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
    global b, l, l2, turn, buttons
    if (b[0] == b[1] == b[2]) or (b[3] == b[4] == b[5]) or (b[6] == b[7] == b[8]) or (b[0] == b[3] == b[6]) or (b[1] == b[4] == b[7]) or (b[2] == b[5] == b[8]) or (b[0] == b[4] == b[8]) or (b[2] == b[4] == b[6]):
        if turn % 2 == 1:
            l = Label(root, text='X wins!', font = ('Courier', 50), bg=color, fg='white')
        else:
            l = Label(root, text='O wins!', font = ('Courier', 50), bg=color, fg='white')
        l.grid(row=4, columnspan=5)
        l2 = Label(root, text='Would you like to play again?', font=('Courier', 25), bg=color, fg='white')
        yes = Button(root, text='Yes', font=('Courier', 18), command=play_again)
        no = Button(root, text='No', font=('Courier', 18), command= end)
        yes.grid(row=6, column=1)
        no.grid(row=6, column=3)
        l2.grid(row=5, columnspan=5)
        for i in buttons:
            i.config(state='disabled')
    else:
        for i in b:
            if i != 'x' and i != 'o':
                tie = False
                break
            tie = True
        if tie:
            l = Label(root, text='It\'s a Tie!', font = ('Courier', 40), bg=color, fg='white')
            l.grid(row=4, columnspan=5)
            l2 = Label(root, text='Would you like to play again?', font=('Courier', 25), bg=color, fg='white')
            l2.grid(row=5, columnspan=5)
            yes = Button(root, text='Yes', font=('Courier', 18), command=play_again)
            no = Button(root, text='No', font=('Courier', 18), command=end)
            yes.grid(row=6, column=1)
            no.grid(row=6, column=3)
        turn += 1

def end():
    exit()

def play_again():
    global buttons, root, b, turn
    turn = 1
    root.destroy()
    root = Tk()
    root.title('Tic Tac Toe!!!')
    root.config(bg=color)
    b = ['1', '2', '3', '4' ,'5', '6', '7', '8', '9']
    buttons = []
    for i in range(9):
        buttons.append(Button(root,font=('Courier', 50), width=3, height=1, command=lambda index=i: press(index)))
    buttons[0].grid(row=1, column=1)
    buttons[1].grid(row=1, column=2)
    buttons[2].grid(row=1, column=3)
    buttons[3].grid(row=2, column=1)
    buttons[4].grid(row=2, column=2)
    buttons[5].grid(row=2, column=3)
    buttons[6].grid(row=3, column=1)
    buttons[7].grid(row=3, column=2)
    buttons[8].grid(row=3, column=3)

    eml = Label(root, width=15, bg=color)
    eml.grid(row=1, column=0)
    emr = Label(root, width=15, bg=color)
    emr.grid(row=1, column=4)
    emt = Label(root, height=5, bg=color)
    emt.grid(row=0)
    l = Label(root, height=5, bg=color)
    l.grid(row=4)
    l2 = ''

for i in range(9):
    buttons.append(Button(root,font=('Courier', 50), width=3, height=1, command=lambda index=i: press(index)))

buttons[0].grid(row=1, column=1)
buttons[1].grid(row=1, column=2)
buttons[2].grid(row=1, column=3)
buttons[3].grid(row=2, column=1)
buttons[4].grid(row=2, column=2)
buttons[5].grid(row=2, column=3)
buttons[6].grid(row=3, column=1)
buttons[7].grid(row=3, column=2)
buttons[8].grid(row=3, column=3)
#em means empty, l means left, r means right, and t means top

eml = Label(root, width=15, bg=color)
eml.grid(row=1, column=0)
emr = Label(root, width=15, bg=color)
emr.grid(row=1, column=4)
emt = Label(root, height=5, bg=color)
emt.grid(row=0)
l = Label(root, height=5, bg=color)
l.grid(row=4)
l2 = ''

root.mainloop()