from Blackjack import Blackjack
import click

@click.command()
def blackjack_manager():
    """Simple game of blackjack"""
    game = Blackjack()
    game.new_game()
    finished_game = False
    while finished_game == False:
        game.print_turn()
        move = click.prompt('Hit or stand?', type=str)
        if move == "Hit":
            Blackjack.player_hit()
        finished_game = True
        
if __name__ == '__main__':
    blackjack_manager()

