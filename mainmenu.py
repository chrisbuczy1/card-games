def menu():
    game = input('What game would you like to play? \n(b = blackjack)\n(y = yahtzee)\n:')
    if game.lower() == 'b':
        import blackjack
    elif game.lower() == 'y':
        import yahtzee

menu()