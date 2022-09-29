# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза
lst = [i for i in input()]
def razvernut(listik):
    i = len(listik) - 1
    res = []
    while i > -1:
        res.append(listik[i])
        i -= 1
    return res
print(razvernut(lst))
