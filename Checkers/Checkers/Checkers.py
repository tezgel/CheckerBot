import board as bd
import Dumb_Bot as db

#change commen5regbfek
#commented

if __name__ == '__main__':
    board = bd.Board()
    bot = db.DumbBot()
    print('Checker Wars')

    playing = True

    while playing:

        board.generate_board()
        print(board.print_player_board())


        board.move_piece()






