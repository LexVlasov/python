class OrgTech:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return 'На склад добавлен {}'.format(self.type)

class Printer(OrgTech):
    def print(self):
        if self.type == 'Принтер':
            return '{} на складе'.format(self.type)
        else:
            return 'Это не принтер'

class Scaner(OrgTech):
    def scaner(self):
        if self.type == 'Сканер':
            return '{} на складе'.format(self.type)
        else:
            return 'Это не сканер'


class Xerox(OrgTech):
    def xerox(self):
        if self.type == 'Ксерокс':
            return '{} на складе'.format(self.type)
        else:
            return 'Это не ксерокс'


org1 = Printer('Принтер')
org2 = Xerox('Принтер')
org3 = Scaner('Принтер')
print(org1.print())
print(org2.xerox())
print(org3.scaner())
print(org3)