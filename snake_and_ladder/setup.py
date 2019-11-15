from models import Board

def create_layout():
    FILEPATH = 'inputs/1.txt'

    board_id = 1
    board_rows = 10
    board_cols = 10

    with open(FILEPATH) as fp:
        number_of_snakes = fp.readline()
        snake_positions = list()
        ladder_positions = list()
        players = list()
        for i in range(1, int(number_of_snakes)):
            snake_positions.append(fp.readline().split(' '))

        number_of_ladders = fp.readline()
        for i in range(1, int(number_of_ladders)):
            ladder_positions.append(fp.readline().split(' '))

        number_of_players = fp.readline()
        for i in range(1, int(number_of_players)):
            players.append(fp.readline())

    board = Board(board_id, board_rows, board_cols,
                  snake_count=number_of_snakes,
                  ladder_count=number_of_ladders,
                  player_count=number_of_players)

    for positions in snake_positions:
        board.place_snake(board_id, int(positions[0]), int(positions[1]))

    for positions in ladder_positions:
        board.place_ladder(board_id, int(positions[0]), int(positions[1]))

    for player in players:
        board.add_player(board_id, player)



if __name__ == '__main__':
    create_layout()

