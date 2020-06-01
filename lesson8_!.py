class Date:
    @staticmethod
    def get_static(input_date):
        data = input_date
        new_data = data.split('-')
        dd = new_data[0]
        mm = new_data[1]
        yy = new_data[2]
        if int(dd) >= 1 and int(dd) <= 31 and int(mm) >= 1 and  int(mm) <=12:
            return print(dd + '.' + mm + '.' + yy)
        else:
            return print("Не верный формат")

    @classmethod
    def get_class(self, input_date):
        self.data = input_date
        new_data = self.data.split('-')
        dd = new_data[0]
        mm = new_data[1]
        yy = new_data[2]
        if int(dd) >= 1 and int(dd) <= 31 and int(mm) >= 1 and int(mm) <= 12:
            return print(dd + '.' + mm + '.' + yy)
        else:
            return print("Не верный формат")




Date.get_static('40-13-2019')
Date.get_class('25-12-2025')
