# задание 2

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        print(mass, 'T')

my_road = Road(20, 7000)
my_road.calc_mass()