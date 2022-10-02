# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)
my_dict = {
    'id1': {
        'email': '1',
        'name': 'misha',
        'surname': 'blabla',
        'telephone number': '+375296330388'
    },
    'id2': {
        'email': '2',
        'name': 'masha',
        'surname': 'blabla2',
        'telephone number': '+3752963303888'
    },
    'id3': {
        'email': '',
        'name': 'vasia',
        'surname': 'blabla3',
        'telephone number': '+37529633038888'
    },
    'id4': {
        'name': 'petya',
        'surname': 'blabla5',
        'telephone number': '+375296330388888'
    }
}
a = my_dict.items()
for i, j in a:
    if 'email' not in j or j.get('email') == '':
        print(j.get('name'))
