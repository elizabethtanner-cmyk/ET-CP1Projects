import random, time
cards = ['A of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'J of Spades', 'Q of Spades', 'K of Spades', \
         'A of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'J of Hearts', 'Q of Hearts', 'K of Hearts', \
         'A of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'J of Clubs', 'Q of Clubs', 'K of Clubs', \
         'A of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'J of Diamonds', 'Q of Diamonds', 'K of Diamonds']
shuffled = []
card = ''
for i in range(len(cards)):
    while card in shuffled:
        card = random.choice(cards)
    if i == 0:
        card = random.choice(cards)
    shuffled.append(card)

hand = [shuffled[0], shuffled[2]]
opposite_hand = [shuffled[1], shuffled[3]]
for i in range(4):
    del shuffled[0]
print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYour hand is: {hand[0]}, {hand[1]}.\n\n\n\n\n\n\n\n')
time.sleep(1)
print('Burning 1 card...\n\n')
del shuffled[0]
time.sleep(1)
table_cards = [shuffled[0], shuffled[1], shuffled[2]]
for i in range(3):
    del shuffled[0]
print('The cards on the table are...')
time.sleep(1)
for i in range(3):
    print(table_cards[i], end='  ')
    time.sleep(.5)


