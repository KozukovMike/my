# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны
my_dict = {
    'Belarus': ['Gomel', 'Minsk', 'Vitebsk'],
    'England': ['London', 'Manchester', 'Liverpool']
}
name_of_city = input()
def get_key(inp_str: str, inp_dict: dict):
    inp_dict = dict(filter(lambda x: inp_str in x[1], inp_dict.items()))
    if len(inp_dict):
        return inp_dict.popitem()[0]
    else:
        return 'такого города не существует)))))))))))))))'
print(get_key(name_of_city, my_dict))
