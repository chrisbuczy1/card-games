from random import choices
import pandas as pd

class yahtzee():
    dice = [1, 2, 3, 4, 5, 6]
    # roll = choice(dice)
    table_dice = []
    player_dice = []
    player2_dice = []
    n = 5

    def play(self):
        print(choices(population=self.dice, k=5))
        


x = yahtzee()
x.play()
