from Blackjack import Blackjack
import click

@click.command()
def blackjack_manager():
    """Simple game of blackjack"""
    blackjack = Blackjack()
    blackjack.new_game()
    finished_game = False
    while finished_game == False:
        blackjack.print_turn()
        move = click.prompt('Hit or stand?', type=str)
        if move == "Hit":
            blackjack.player_hit()
        if move == "Stand":
            blackjack.player_stand()
        if blackjack.winner:
            print(blackjack.win_message)
            finished_game = True
        
if __name__ == '__main__':
    blackjack_manager()

