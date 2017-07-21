class Board:

    def __init__(self):
        self.available_moves = [num for num in range(9)]
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.horizontal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.vertical = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
        self.diagonal = [[0, 4, 8], [2, 4, 6]]
        self.win_conditions = self.horizontal + self.vertical + self.diagonal

    def move(self, player, tile):
        if tile in self.available_moves:
            self.available_moves.remove(tile)
            self.board[tile] = player.symbol

    def win(self):

        for condition in self.win_conditions:
            tiles = []
            for index in condition:
                tiles.append(self.board[index])

            if len(set(tiles)) == 1 and ' ' not in tiles:
                return True

    def tie(self):
        if ' ' not in self.board:
            return True

    def show_board(self):

        row = '---+---+---\n'
        board = ''
        for i in range(0, 9, 3):
            board += ' {} | {} | {}\n'.format(self.board[i], self.board[i+1], self.board[i+2])
            if i != 6:
                board += row

        print(board)
