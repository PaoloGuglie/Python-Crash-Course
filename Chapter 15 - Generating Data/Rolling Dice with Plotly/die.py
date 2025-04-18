from random import randint


class Die:

    def __init__(self, sides: int = 6):

        self.sides = sides

    def roll(self):
        return randint(1, self.sides)
