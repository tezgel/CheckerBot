import board as bd
import move as mv
import player as p
import random as rand


class DumbBot:
    def __init__(self):
        self.x_locations = []   # tracks all positions of x pieces
        self.o_locations = []   # tracks all positions of o pieces

# Searches game board for starting point of all pieces and appends them to locations list
    def dumb_helper(self, grid):
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if col == 'x' or col == 'X':
                    self.x_locations.append([x, y])

                if col == 'o':
                    self.o_locations.append([x, y])

    def is_jumpable(self):
        pass

#Teke Code
class RandomMove:
    def __init__(self, arraySize):
        self.arraySize = arraySize

    def set_movenum(self, arraySize, num):
        self.num = random.randint(0, arraySize-1) 

# Demo of labeled board
Bd = bd.Board()
Bd.generate_board()         # Small bug w/ row[0] it has a 9th spot
Bd.print_player_board()
q_grid = Bd.grid

# Demo of DumbBot
Db = DumbBot()
print(Db.dumb_helper(q_grid))

#Teke Code

Mv = RandomMove()
Mv.set_movenum(len(Db.x_locations), 0)


print(Db.x_locations)
print(Db.o_locations)
print('_____' * 8)
print('Figuring out jumps based off coordinates \n')


Bd.move_piece('o', 6, 1, 5, 2)
Bd.move_piece('o', 5, 2, 4, 3)
new_move = Bd.grid
Bd.print_player_board()
print('\nX locations can jump o which is at ')
print(Db.x_locations[8])
print(Db.x_locations[9])
Db.dumb_helper(new_move)
print('Jumpable O coordinates', Db.o_locations[12])


