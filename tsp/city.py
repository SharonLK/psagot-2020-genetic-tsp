import math


class City:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance(self, city: 'City') -> float:
        return math.sqrt((self.x - city.x) ** 2 + (self.y - city.y) ** 2)
