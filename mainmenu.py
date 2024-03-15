def menu():
    game = input('What game would you like to play? \n(b = blackjack)\n(p = poker)\n:')
    if game.lower() == 'b':
        import blackjack
    elif game.lower() == 'p':
        import poker

menu()