from setup import create_layout
from models import Game

def start_game(board):
    g = Game(board)
    players = board.players

    while all(player.get_current_position() != board.layout.length for player in players):
        for player in players:
            g.player_chance(player)


    for player in players:
        if player.get_current_position() != board.layout.length:
            print('{} wins the game'.format(player.name))

if __name__ == '__main__':
    board = create_layout()
    start_game(board)