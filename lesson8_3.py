class Return:
    def __str__(self):
        end_data = []
        while True:
            self.data = input('Введите данные через запятую или введите "stop":')
            if type(self.data) == int or type(self.data) == str:
                new_data = self.data.split(',')
                for i in new_data:
                    if i == 'stop' or i == 'Stop':
                        return str(end_data)
                        break
                    else:
                        end_data.append(i)
                        print(str(end_data))
            else:
                'Не верный формат!'

oko = Return()

print(oko)
