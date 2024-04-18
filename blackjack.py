from random import choice

class blackjack():
    dealers_hand = []
    players_hand = []
    deck = ['a', 'a', 'a', 'a', 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9,
                9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, ]
    
   
    #starting menu and declare deck copy and hand copy variables
    def play(self):
        self.deck = ['a', 'a', 'a', 'a', 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9,
                9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, ]
        self.dealers_hand = []
        self.players_hand = []
        x = input('would you like to play blackjack? (y or n)')
        if x.lower() == 'y':
            self.game()
        elif x.lower() == 'n':
            exit()

    
    #add card to specified players hand
    def addcard(self, hand,):
        _ = choice(self.deck)
        self.deck.remove(_)
        hand.append(_)
        
    
    #playing game, adding cards to players and dealers hand, ace logic
    def game(self):
        self.addcard(self.players_hand) 
        if self.players_hand[0] == 'a':
                print(self.players_hand)
                ace = input('You got an ace, do you want a one or eleven? ')
                if ace == '1':
                    self.players_hand[0] = 1
                elif ace == '11':
                    self.players_hand[0] = 11
        self.addcard(self.dealers_hand)
        self.one_or_eleven()
        self.addcard(self.players_hand) 
        if self.players_hand[1] == 'a':
                print(self.players_hand)
                ace = input('You got an ace, do you want a one or eleven? ')
                if ace == '1':
                    self.players_hand[1] = 1
                elif ace == '11':
                    self.players_hand[1] = 11
        self.addcard(self.dealers_hand)
        print(f'{self.dealers_hand[1:]}{self.players_hand}')
        self.one_or_eleven()
        self.sorh()

    
    #hit or stand logic
    def sorh(self):
        hors = input('hit or stand? (h or s)')
        while hors == 'h':
            if hors.lower() == 'h':
                self.addcard(self.players_hand)
                print(f'{self.dealers_hand[1:]}{self.players_hand}')
                
                if self.players_hand[-1] == 'a':
                    ace = input('You got an ace, do you want a one or eleven? ')
                    if ace == '1':
                        self.players_hand[-1] = 1
                    elif ace == '11':
                        self.players_hand[-1] = 11
                
                if sum(self.players_hand) > 21: 
                    self.check()
            hors = input('hit or stand? (h or s)')

      

        if hors.lower() == 's':
            while sum(self.dealers_hand) < 17:
                self.addcard(self.dealers_hand)
                self.one_or_eleven()
            print(f'{self.dealers_hand}{self.players_hand}')
            self.check()
    
    
    #ace logic
    def one_or_eleven(self):
        if 'a' in self.dealers_hand:
            self.dealers_hand.remove('a')
            if 11 + sum(self.dealers_hand) <= 10:
                self.dealers_hand.append(11)
            elif 1 + sum(self.dealers_hand) <= 20:
                self.dealers_hand.append(1)
            
                
    
    #check who won
    def check(self):
        if sum(self.players_hand) > 21:
            print('Bust!')
            self.play()
        elif sum(self.dealers_hand) > 21:
            print('You win!')
            self.play()
        elif sum(self.players_hand) > sum(self.dealers_hand):
            print('You won!')
            self.play()
        elif sum(self.players_hand) < sum(self.dealers_hand):
            print('You Lost!')
            self.play()
        else:
            print('Push')
            self.play()




x = blackjack()

x.play()

    


