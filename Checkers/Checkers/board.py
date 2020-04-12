# We will represent Kings as capital letters
# Also, X will always start on bottom, and Circles will always start on top

#this is a new change
class Board:
    def __init__(self):
        self.dimensions = 9
        self.grid = []
        self.x_direction = 'down'
        self.o_direction = 'up'

    def is_on_board(self, row, col):
        return 1 <= row < self.dimensions-1 and \
            1 <= col < self.dimensions-1

    # Generates new board
    def generate_board(self):
        # Create player board
        for player_row in range(self.dimensions):
            self.grid.append([])

            for i, player_col in enumerate(range(self.dimensions)):
                if player_col == 0:
                    self.grid[player_row].append(str(i + player_row))
                    self.grid[player_col].append(str((i + 1) + player_row))

                elif player_row == 0:
                    break

                else:
                    self.grid[player_row].append('.')   # Creates board full of blank spots

        # Creates pieces in starting positions
        for col in range(self.dimensions):
            for row in range(self.dimensions):
                if (row + col) % 2 == 1:  # if spot is technically accessible
                    if 0 < row < 4 and col > 0:  # Initializes x for top of board
                        self.grid[row][col] = 'x'
                    if row > 5 and col > 0:  # Initializes o for bottom of board
                        self.grid[row][col] = 'o'

    # Print player board
    def print_player_board(self):
        for player_row in self.grid:
            print(" ".join(player_row))

    # Returns point at given row and column value
    def get_point(self, row, col):
        return self.grid[row][col]

    def point_available(self, row, col):
        if self.get_point(row, col) == '.' and (row + col) % 2 == 1: # If point is empty and is valid
            return True
        else:
            return False

    def set_point(self, row, col, value):
        self.grid[row][col] = value

    def move_piece(self, player_value, old_row, old_col, new_row, new_col): # Moves piece from previous location
        # todo implement player to prevent a player moving an enemy piece,

        direction = self.get_direction(old_row, old_col)
        # If move is in correct direction and new point is available
        if self.in_correct_direction(direction, old_row, new_row) and self.point_available(new_row, new_col):

            # If new point is a neighbor of old point
            if self.is_neighbor(old_row, old_col, new_row, new_col):
                self.set_point(new_row, new_col, self.get_point(old_row, old_col)) # Put value of old spot into new spot
                self.set_point(old_row, old_col, '.')    # replace value of old spot with .
                # todo update either x_location or o_location from dumbBot from old rol col to new rol col

            # If new point is reachable by a jump
            elif self.is_jumpable(player_value, old_row, old_col, new_row, new_col):
                self.set_point(new_row, new_col, self.get_point(old_row, old_col)) # Put value of old spot into new spot
                self.set_point(old_row, old_col, '.')  # replace value of old spot with .
                # todo update either x_location or o_location from dumbBot from old rol col to new rol col

            else:
                print("Moving a piece here is not permitted")

        else:   # piece cannot move in that direction
            print("Piece cannot move in that direction")

    def neighbor_points(self, row, col): # Determines the direct neighbors to a given point may move to.
        p1 = (row - 1, col - 1)
        p2 = (row - 1, col + 1)
        p3 = (row + 1, col - 1)
        p4 = (row + 1, col + 1)
        points = [p1, p2, p3, p4]
        neighbor_points = []

        for point in points:
            if self.is_on_board(point[0], point[1]):
                neighbor_points.append(point)
            elif not self.is_on_board(point[0], point[1]):
                neighbor_points.append(None)
        # Must account for points that are jump points
        return neighbor_points

    # Returns true if point is a neighbor, false if not a neighbor
    def is_neighbor(self, old_row, old_col, new_row, new_col):
        t1 = (new_row, new_col)
        if t1 in self.neighbor_points(old_row, old_col):    # If the spot is a neighboring point
            return True
        else:
            return False

    def get_direction(self, row, col):
        if self.grid[row][col] == 'x':
            return self.x_direction
        if self.grid[row][col] == 'o':
            return self.o_direction
        else:
            return None

    def in_correct_direction(self, direction, old_row, new_row):
        if direction == 'down' and old_row - new_row < 0:
            return True
        if direction == 'up' and old_row - new_row > 0:
            return True
        if direction == None:
            return True
        else:
            return False

    def is_jumpable(self, player_value, old_row, old_col, new_row, new_col):
        # todo implement player to check if neighbor is an enemy piece
        jump_direction = self.get_jump_direction(old_row, old_col, new_row, new_col) # Find direction of jump neighbor

        # If the neighbor
        # Find direct neighbor in the same direction
        direct_neighbor = self.neighbor_points(old_row, old_col)[jump_direction]

        if direct_neighbor is not "." and direct_neighbor is not player_value: #if the piece to be jumped is an enemy
            self.remove_piece(direct_neighbor[0],direct_neighbor[1]) # Remove the jumped piece
            return True
        else:
            return False

    def get_jump_direction(self, old_row, old_col, new_row, new_col):
        # 0 == up left, 1 == up right, 2 == down left, 3 == down right
        if old_row - new_row < 0: # Down
            if old_col - new_col < 0: # Right
                return 3
            elif old_col - new_col > 0: # Left
                return 2
        elif old_row - new_row > 0: # Up
            if old_col - new_col < 0: # Right
                return 1
            elif old_col - new_col > 0: # Left
                return 0

    def remove_piece(self, row, col):
        self.grid[row][col] = '.'



# Demo on Board Structure
B = Board()
B.generate_board()
#print(B.print_player_board())
#print(B.grid)
#print(B.get_point(2,3))
#print(B.point_available(2,3))
#B.set_point(2,3,"X")
#print(B.get_point(2,3))
print(B.print_player_board())
B.move_piece("o",6,1,5,2)
print(B.print_player_board())
B.move_piece("x",3,2,4,3)
print(B.print_player_board())
B.move_piece("x",4,3,7,2)
print(B.print_player_board())
B.move_piece("x",4,3,6,2)
print(B.print_player_board())




