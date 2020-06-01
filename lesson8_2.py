class DellNull():
    def __init__(self, x):
        self.x = x

    def __truediv__(self, other):
        try:
            return float(self.x / other.x, 2)
        except:
            return 'Бесконечное число'

a = DellNull(10)
b = DellNull(0)

print(a/b)

