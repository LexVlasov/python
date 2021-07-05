
def resume():
    anketa = {'Имя': '', 'Фамилия': '', 'Год рождения': '', 'Город': '', 'email': '', 'Телефон': ''}
    conclusion = {'Имя': [], 'Фамилия': [], 'Год рождения': [], 'Город': [], 'email': [], 'Телефон': []}
    for f in anketa.keys():
        user_data = input('{}:'.format(f))
        anketa[f] = int(user_data) if (f == 'Год рождения' or f == 'Телефон') else user_data
        conclusion[f].append(anketa[f])
    return conclusion.values()


info = resume()
print(info)
