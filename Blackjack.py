from Deck import Deck

class Blackjack(self):

    def __init__(self, initial_balance):
        self.player_hand = []
        self.dealer_hand = []
        
        self.player_tot = 0
        self.dealer_tot = 0

        self.winner = False

        self.deck = Deck()
        self.deck.init_deck()

    def player_hit(self):
        self.player_hand.append(self.deck.draw())
        calc_total("Player")

    def player_stand(self):
        self.check_winner()

    def dealer_hit(self):
        self.dealer_hand.append(self.deck.draw())
        calc_total("Dealer")

    def calc_total(self, who):
        if who == "Player":
            hand = self.player_hand
            total = self.player_tot
        else:
            hand = self.dealer_hand
            total = self.dealer_tot
        aces = 0
        for card in hand:
            if card.value in "JQK":
                total += 10
            elif card.value in "2345678910":
                total += int(card.value)
            else:
                aces += 1
        if aces:
            total += aces
            while aces > 0:
                if total < 21:
                    total+10
                aces -= 1
        if total > 21:
            self.check_winner()

    def dealers_turn(self):
        while self.dealer_tot < 17:
            self.dealer_hit()
        self.check_winner()
    
    def check_winner(self):
        if self.player_tot > 21:
            self.winner = "Dealer"    
        elif self.player_tot == 21:
            if self.dealer_tot == 21:
                self.winner = "Draw"
            elif self.player_tot > self.dealer_tot:
                self.winner = "Player"
        else self.player_tot < 21:
            if self.dealer_tot > self.player_tot:
                self.winner = "Dealer"
            elif self.dealer_tot == self.player_tot:
                self.winner = "Draw"
            else:
                self.winner = "Player"

    def new_game(self):
        self.deck.init()  
        
        self.player_hit()
        self.dealer_hit()
        self.player_hit()
        self.dealer_hit()

if __name__ == "__main__":
    deck = Deck()
    print(deck.cards)
