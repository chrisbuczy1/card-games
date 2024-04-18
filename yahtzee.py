from random import choices
import pandas as pd

class yahtzee():
    dice = [1, 2, 3, 4, 5, 6]
    rolls = 3
    x = 5
    dices = []

    #roll dice
    def roll(self):
        self.table_dice = choices(population=self.dice, k=self.x)

    #appends kept dice into your hand
    def keep(self):    
        self.player_dice = input('Which dice would you like to keep\n(type number with spaces between)? ')
        self.player_dice = self.player_dice.split()
        self.player_dice = [int(x) for x in self.player_dice]
        self.dices.extend(self.player_dice)

        
    #main game and amount of dice rolls logic
    def play(self):
        while self.rolls != 0:
            self.roll()
            print(f'\n{self.table_dice}')
            self.keep()
            for num in self.player_dice:
                if num in self.table_dice:
                    self.table_dice.remove(num)
                    self.x = len(self.table_dice)
                else:
                    self.keep()
                    break
            self.rolls -= 1
            print(f'Rolls left: {self.rolls}')
            print(self.player_dice)
        


        


x = yahtzee()
x.play()
