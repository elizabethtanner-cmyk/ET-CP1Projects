#Elizabeth Tanner
#Tic Tac Toe

s = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  #spaces in board

name = ''
x_or_o = 'X'
p2 = 'O'
turn = 1

def main():       #main function
    global x_or_o, p2, s, spaces, turn, name
    if turn > 1:
        rating = input('Please rate this game out of 5 stars: ')
        if '5' in rating or 'five' in rating:
            print('Thank you for the 5 star rating!')
        else:
            print('Thank you for your feedback!')
        ans = input('Please leave a review! (This is not an option! You must write your review)\n')
        print('\n\nYour review has been saved!\n\n\n"' + ans + '"')
    else:
        print('What\'s your name?')
        name = input()
    turn = 1
    s = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    #welcome message
    print('_________________________________________________________')
    print('Welcome to Tic Tac Toe, '+ name + '!!!!')
    print('You will be given the option to be X or O.')
    print('No matter what you choose, you will go first.')
    print('So far you must verse a real person, but computers\nare coming soon')
    #print('***Note: Computers are simple and easy to beat***') #add this when i code in a computer
    print('_________________________________________________________')
    print('Press enter to continue.')
    input()
    #choose what they will be
    print('\n'*50)
    ans = input('Would you like to be \n  1. X\n  2. O\n') 
    if ans == '2':
        x_or_o = 'O'
        p2 = 'X'                          
    print('\n'*50)
    input('For now we only have a 2 person option, okay?\n')
    tic_tac_toe()


def print_board():  #prints the board
    global s
    print(f'  {s[0]} | {s[1]} | {s[2]}')
    print('____|___|____')
    print(f'  {s[3]} | {s[4]} | {s[5]}')
    print('____|___|____')
    print(f'  {s[6]} | {s[7]} | {s[8]}')
    print('    |   |')


def tic_tac_toe():
    global spaces, s, turn
    print('\n'*50)
    print_board()
    print('\n'*3)
    if turn % 2 ==1:  #if the turn is divisible by one it is player ones turn
        print('Player 1')
        print('_____________')
        sign = x_or_o
    else:
        print('Player 2')
        print('_____________')
        sign = p2
    while True:
        space = input('Please enter in the number of space you would like to take: ')
        try:           #error proofs the int(space) and accessing the index in s
            space = int(space)
            if s[space - 1] == str(space):
                break
            print('It must be an unoccupied square.')

        except:                                              
            print('Please only enter a NUMBER 1-9')
    s[space - 1] = sign
    turn += 1
    print(sign)
    check_win(sign)


def check_win(sign):
    global s
    if (s[0] == s[1] == s[2] == sign) or (s[3] == s[4] == s[5] == sign) or (s[6] == s[7] == s[8] == sign) or (s[0] == s[3] == s[6] == sign) or (s[1] == s[4] == s[7] == sign) or (s[2] == s[5] == s[8] == sign) or (s[0] == s[4] == s[8] == sign) or (s[2] == s[4] == s[6] == sign):
        print_board()
        if sign == x_or_o:
            print('\n'*50 +'Player 1 Wins!!!!!')
        else:
            print('\n'*50 +'Player 2 Wins!!!!!')
        print('Would you like to play again? (y/n)')
        ans = input()
        if 'y' in ans:  # using "in" in case they decide to not listen to me and type yes, yeah, or anything like that
            main()
    else:
        tie = True
        for i in s:
            if i != 'X' and i != 'O':
                tie = False           #if there isnt an x or o then it is empty and unchosen. thus it can't be a tie.
                break
        if not tie:
            tic_tac_toe()
        else:
            print_board()
            print('\n'*50 +'It\'s a tie!!! Would you like to play again? (y/n)')
            ans = input()
            if 'y' in ans: 
                main()
            #no need for an else to stop it

main()