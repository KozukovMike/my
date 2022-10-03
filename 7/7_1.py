text = '''
iPhone 14 Pro Max

ru from 1 1800

ru from 5 1700

en from 1 1600

iPhone 14 Pro

ru from 50 1500

en from 5 1400

en from 20 1300
'''
countries = ['ru', 'en', 'fr', 'ch']
from_to = ['from 1', 'from 5', 'from 20', 'from 50']
list_of_strings = text.split('\n')
list_of_strings = [i for i in list_of_strings if i != '']
res_dict = {}
for st in list_of_strings:
    list_of_words_in_st = st.split()
    if list_of_words_in_st[0] not in countries:
        res_dict[st] = {} # вписываем новый телефон
        name_of_phone = st # запомнили название телефона (ключа)
    else:
        if list_of_words_in_st[0] not in res_dict[name_of_phone]: # проверка есть ли название страны в словаре конкретного телефона
            res_dict[name_of_phone][list_of_words_in_st[0]] = {}
            res_dict[name_of_phone][list_of_words_in_st[0]][list_of_words_in_st[1] + ' ' + list_of_words_in_st[2]] = list_of_words_in_st[3]
        else:
            res_dict[name_of_phone][list_of_words_in_st[0]][list_of_words_in_st[1] + ' ' + list_of_words_in_st[2]] = list_of_words_in_st[3]
print(res_dict)
