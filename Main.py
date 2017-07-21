from GameWorld import GameWorld


if __name__ == '__main__':

    game = GameWorld()
    game.init_players()
    game.board.show_board()
    print("{} starts.".format(game.players[0].symbol))

    while True:
        game.next_round()

        if game.board.win():
            print("{}'s have won.".format(game.players[game.turn].symbol))
            break

        elif game.board.tie():
            print("It's a draw.")
            break

        game.switch_turn()