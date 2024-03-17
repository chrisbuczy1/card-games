from random import choices
import pandas as pd

class yahtzee():
    dice = [1, 2, 3, 4, 5, 6]
    # roll = choice(dice)
    player2_dice = []
    n = 5

    def roll(self):
        self.table_dice = choices(population=self.dice, k=5)
        

    def play(self):
        self.roll()
        print(self.table_dice)
        player_dice = input('Which dice would you like to keep\n(type number with spaces between)? ')
        player_dice = player_dice.split()
        player_dice = [int(x) for x in player_dice]
        for x in player_dice:    
            while x not in self.table_dice:
                player_dice = input('Try again: ')
                player_dice = player_dice.split()
                player_dice = [int(x) for x in player_dice]
                print(player_dice)

        print(player_dice)


        


x = yahtzee()
x.play()
