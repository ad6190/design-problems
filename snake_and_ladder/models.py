import random

class Board:
    def __init__(self, id, rows, cols, snake_count, ladder_count, player_count=2, dice_count=2):
        self.id = id
        self.layout = list()
        self.rows = rows
        self.cols = cols
        self.snakes_count = snake_count
        self.ladder_count = ladder_count
        self.player_count = player_count
        self.dice_count = dice_count
        self.snakes = list()
        self.ladders = list()
        self.players = list()
        self.snake_map = dict()
        self.ladder_map = dict()

    def place_snake(self, board_id, start_pos, end_pos):
        assert board_id == self.id
        self.snakes.append(Snake(start_pos, end_pos))
        self.snake_map[start_pos] = end_pos


    def place_ladder(self, board_id, start_pos, end_pos):
        assert board_id == self.id
        self.ladders.append(Ladder(start_pos, end_pos))
        self.ladder_map[start_pos] = end_pos

    def add_player(self, board_id, name):
        assert board_id == self.id
        assert name not in self.players
        self.players.append(Player(name))


    def setup_board(self):
        for i in range(0, self.rows * self.cols):
            self.layout[i] = i+1


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
        self.current_position = 0

    def set_current_position(self, board, movement_count):
        last_position = self.current_position
        self.current_position = last_position + movement_count
        if self.current_position in board.snake_map:
            snake_end = board.snake_map[self.current_position]
            self.current_position = snake_end
        elif self.current_position in board.ladder_map:
            ladder_end = board.snake_map[self.current_position]
            self.current_position = ladder_end
        return self.current_position

    def get_current_position(self):
        return self.current_position


class Dice:
    def __init__(self, faces=6, fairness=1):
        self.faces = faces
        self.fairness = fairness

    def roll_a_dice(self):
        return random.randint(1, self.faces)

class Game:
    def __init__(self, board):
        self.board = board
        self.dice = Dice()
        self.player_position_map = dict()
        for player in board.players:
            self.player_position_map[player] = 0

    def player_chance(self, player):
        move = self.dice.roll_a_dice()

        last_position = player.get_current_position()
        player.set_current_position(self.board, move)
        current_position = player.get_current_position()

        print("{} rolled a {} and moved from {} to {}".format(player.name, move, last_position, current_position))






