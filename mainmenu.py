def menu():
    game = input('What game would you like to play? \n(b = blackjack)\n(p = poker)\n:')
    if game.lower() == 'b':
        exec(open('blackjack.py').read())
    elif game.lower() == 'p':
        exec(open('poker.py').read())

menu()