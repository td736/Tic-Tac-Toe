from Player import Player
from Board import Board


class GameWorld:

    def __init__(self):
        self.players = []
        self.board = Board()
        self.symbols = ['X', 'O']
        self.turn = 0

    def init_players(self):
        for i in range(2):
            self.players.append(Player(self.symbols[i]))

    def next_round(self):
        print("Available moves are: \n{}".format(self.board.available_moves))
        self.board.move(self.players[self.turn], int(input("Pick a tile: ")))
        self.board.show_board()

    def switch_turn(self):
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0


