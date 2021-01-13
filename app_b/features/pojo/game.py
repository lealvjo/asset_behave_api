class Game(object):
    def __init__(self):
        self.__game = {}

    def set_field_game(self, field, value):
        self.__game[field] = value

    def get_body_game(self):
        return self.__game
