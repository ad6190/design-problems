class Board:
    def __init__(self, id, rows, cols, snake_count, ladder_count, player_count=2, dice_count=2):
        self.id = id
        self.layout = list(list())
        self.rows = rows
        self.cols = cols
        self.snakes_count = snake_count
        self.ladder_count = ladder_count
        self.player_count = player_count
        self.dice_count = dice_count
        self.snakes = list()
        self.ladders = list()
        self.players = list()

    def place_snake(self, board_id, start_pos, end_pos):
        assert board_id == self.id
        self.snakes.append(Snake(start_pos, end_pos))


    def place_ladder(self, board_id, start_pos, end_pos):
        assert board_id == self.id
        self.ladders.append(Ladder(start_pos, end_pos))

    def add_player(self, board_id, name):
        assert board_id == self.id
        assert name not in self.players
        self.players.append(Player(name))


    def setup_board(self):
        display_number = 0
        for i in self.rows:
            for j in self.cols:
                display_number += 1
                self.layout[i][j] = display_number


class Snake:
    def __init__(self, start_pos, end_pos):
        assert start_pos > end_pos, "Snake should bring a player down"
        self.start_pos = start_pos
        self.end_pos = end_pos


class Ladder:
    def __init__(self, start_pos, end_pos):
        assert start_pos < end_pos, "Ladder should take a player up"
        self.start_pos = start_pos
        self.end_pos = end_pos


class Player:
    def __init__(self, name):
        self.name = name


class Dice:
    def __init__(self, faces=6, fairness=1):
        self.faces = faces
        self.fairness = fairness


class Score:
    def __init__(self, board_id, player):
        self.board_id = board_id
        self.player = player






