from Deck import Deck

class Blackjack():

    def __init__(self):
        self.player_hand = []
        self.dealer_hand = []
        
        self.player_tot = 0
        self.dealer_tot = 0

        self.winner = False
        self.win_message = ""

        self.deck = Deck()


    def print_turn(self):
        print("Player has: ")
        for card in self.player_hand:
            print(card.value)

        print("")

        print("Total: ")
        print(self.player_tot)

        print("")

        print("Dealer card: ")
        print(self.dealer_hand[0].value)

        print("")

    def player_hit(self):
        self.player_hand.append(self.deck.draw())
        self.calc_total("Player")

    def player_stand(self):
        self.check_winner()

    def dealer_hit(self):
        self.dealer_hand.append(self.deck.draw())
        self.calc_total("Dealer")

    def calc_total(self, who):
        total = 0
        if who == "Player":
            hand = self.player_hand
        else:
            hand = self.dealer_hand
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
        
        if who == "Player":
            self.player_tot = total
        else:
            self.dealer_tot = total
        
        if self.player_tot > 21:
            self.check_winner()

    def dealers_turn(self):
        while self.dealer_tot < 17:
            self.dealer_hit()
        self.check_winner()
    
    def check_winner(self):
        if self.player_tot > 21:
            self.winner = "Dealer"
            self.win_message = "Player went bust"

        elif self.player_tot == 21:

            if self.dealer_tot == 21:
                self.winner = "Draw"
                self.win_message = "Draw on blackjack"

            elif self.player_tot > self.dealer_tot:
                self.winner = "Player"
                self.win_message = "Blackjack!"

        else:
            
            if self.dealer_tot > self.player_tot:
                self.winner = "Dealer"
                self.win_message = "Dealer wins the game"
            
            elif self.dealer_tot == self.player_tot:
                self.winner = "Draw"
                self.win_message = "Game is a draw"
            
            else:
                self.winner = "Player"
                self.win_message = "Player wins the game"

    def new_game(self):
        self.deck.init()
        
        self.player_hand = []
        self.dealer_hand = []
        self.player_tot = 0
        self.dealer_tot = 0

        self.player_hit()
        self.dealer_hit()
        self.player_hit()
        self.dealer_hit()

if __name__ == "__main__":
    deck = Deck()
    print(deck.cards)
