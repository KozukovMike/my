import random
import copy
import time
t0 = time.time()
sudoku_fild = [[0 for i in range(9)]for j in range(9)] # чисто поле судоку
sudoku_fild_copy = copy.deepcopy(sudoku_fild)
list_till9 = [1, 2, 3, 4, 5, 6, 7, 8, 9] # чисто лист с цифрами от 1 до 9
list_of_81filds = [i for i in range(1, 82)] # чисто лист с 81 номером ячеек
# for i in range(9): # вывод на экран судоку
#     for j in range(9):
#         print(sudoku_fild[i][j], end=' ')
#     print()        # конец вывода
# for i in range(len(list_till9)):# заполняю рандомно первые 9 ячеек
# блок из заполнения первых 4 ячеек рандомно
buf_list_of9 = list_till9.copy()
for i in range(3):
    for j in range(3):
        digit = random.choice(buf_list_of9)
        sudoku_fild[i][j] = digit
        del buf_list_of9[buf_list_of9.index(digit)]
# конец блока


def get_list_of_numbers(sudoku, ind_of_string, ind_of_colomn):
    """
    функция которая возвращает список элементов не доступных для данной ячейки
    :param sudoku: поле судоку
    :param ind_of_string: индекс строки данной ячейки
    :param ind_of_colomn: индекс стобца данной ячейки
    :return: список элементов недоступных для ячейки
    """
    set_of_free_digits = set()
    for j in range(ind_of_colomn):
        set_of_free_digits.add(sudoku[ind_of_string][j])
    for i in range(ind_of_string):
        set_of_free_digits.add(sudoku[i][ind_of_colomn])
    for i in range((ind_of_string // 3) * 3, ((ind_of_string // 3) + 1) * 3):
        for j in range((ind_of_colomn // 3) * 3, ((ind_of_colomn // 3) + 1) * 3):
            set_of_free_digits.add(sudoku[i][j])
    return list(set_of_free_digits)

buf_list_of9 = list_till9.copy()
k = 3
flag = False
while k < 9:
    if k == 3:
        sudoku_fild_copy3 = copy.deepcopy(sudoku_fild)
    if k == 4:
        sudoku_fild_copy4 = copy.deepcopy(sudoku_fild)
    if k == 5:
        sudoku_fild_copy5 = copy.deepcopy(sudoku_fild)
    if k == 6:
        sudoku_fild_copy6 = copy.deepcopy(sudoku_fild)
    if k == 7:
        sudoku_fild_copy7 = copy.deepcopy(sudoku_fild)
    if k == 8:
        sudoku_fild_copy8 = copy.deepcopy(sudoku_fild)
    for j in range(k): # тут i будет = k
        list_of_unavailable_numbers = get_list_of_numbers(sudoku_fild, k, j)
        list_of_available_numbers = list(set(buf_list_of9).difference(list_of_unavailable_numbers))
        if list_of_available_numbers == []:
            flag = True
            break
        sudoku_fild[k][j] = random.choice(list_of_available_numbers)
    for i in range(k + 1): # тут j будет = k
        list_of_unavailable_numbers = get_list_of_numbers(sudoku_fild, i, k)
        list_of_available_numbers = list(set(buf_list_of9).difference(list_of_unavailable_numbers))
        if list_of_available_numbers == []:
            flag = True
            break
        sudoku_fild[i][k] = random.choice(list_of_available_numbers)
    if flag:
        if k == 5:
            sudoku_fild = copy.deepcopy(sudoku_fild_copy4)
            k -= 2
        if k == 6:
            sudoku_fild = copy.deepcopy(sudoku_fild_copy4)
            k -= 3
        if k == 7:
            sudoku_fild = copy.deepcopy(sudoku_fild_copy5)
            k -= 3
        if k == 8:
            sudoku_fild = copy.deepcopy(sudoku_fild_copy6)
            k -= 3
        flag = False
    print('\n\n\n')
    for i in range(9):  # вывод на экран судоку
        for j in range(9):
            print(sudoku_fild[i][j], end=' ')
        print()  # конец вывода
    k += 1


print('\n\n\n\n\n')
for i in range(9): # вывод на экран судоку
    for j in range(9):
        print(sudoku_fild[i][j], end=' ')
    print()        # конец вывода
t1 = time.time()
print(t1 - t0)
def valid_solution(sudoku):
    #print('\n'.join(map(str, sudoku)))
    buf = 0
    for i in sudoku:
        if len(set(i)) != len(i):
            return False
    lst = [[sudoku[i][j] for i in range(9)] for j in range(9)]
    for i in lst:
        if len(set(i)) != len(i):
            return False
    lst = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
    buf = 0
    for j in lst:
        k = []
        for i in range(j[0], j[0] + 3):
            for lst in range(j[1], j[1] + 3):
                k.append(sudoku[i][lst])
        if len(set(k)) != 9:
            return False
    for j in sudoku:
        if 0 in j:
            return False
    return True
print(valid_solution(sudoku_fild))
