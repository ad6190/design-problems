from setup import create_layout
from models import Game

def start_game(board):
    g = Game(board)
    players = board.players
    board_length = len(board.layout)
    while all(player.get_current_position() < board_length for player in players) :
        for player in players:
            g.player_chance(player)
            if player.get_current_position() == board_length:
                break

    for player in players:
        if player.get_current_position() == board_length:
            print('{} wins the game'.format(player.name))

if __name__ == '__main__':
    board = create_layout()
    start_game(board)