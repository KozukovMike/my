sentense = input()
number_of_spaces = sentense.count(' ')
print('first way:', sentense.replace(' ', '-', number_of_spaces))
# value_of_r_spaces = len(sentense) - len(sentense.rstrip(' '))
# value_of_l_spaces = len(sentense) - len(sentense.lstrip(' '))
# print('-'*value_of_l_spaces + '-'.join(sentense.split()) + '-'*value_of_r_spaces)
# пока не придумал 2 способ без цикла
result = ''
for i in sentense:
    if i == ' ':
        result += '-'
    else:
        result += i
print(result)