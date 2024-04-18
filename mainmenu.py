class menu():
    def main_menu(self):
        game = input('What game would you like to play? \n(b = blackjack)\n(y = yahtzee)\n:')
        if game.lower() == 'b':
            import blackjack
        elif game.lower() == 'y':
            import yahtzee

player = menu()
player.main_menu()