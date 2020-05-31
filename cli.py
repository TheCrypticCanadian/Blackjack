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
        move = click.prompt('Hit(1) or stand?(2)', type=str)
        if move == '1':
            blackjack.player_hit()
        if move == '2':
            blackjack.player_stand()
        if blackjack.winner:
            blackjack.print_turn()
            finished_game = True
        
if __name__ == '__main__':
    blackjack_manager()

