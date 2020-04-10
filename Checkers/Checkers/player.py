import enum


class Player(enum.Enum):
    def __init__(self):
        self.prev_spot = None
        self.new_spot = None

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white

    def prompt_player(self):
        self.prev_spot = input('Enter the coordinates of piece you want to move: ')
        self.new_spot = input('Enter Spot where you want to move piece: ')

    def get_prev_spot(self):
        return self.get_prev_spot()

    def get_new_spot(self):
        return self.get_new_spot()


