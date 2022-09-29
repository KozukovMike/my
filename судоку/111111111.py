import random
sudoku_fild = [[0 for i in range(9)]for j in range(9)] # чисто поле судоку
list_till9 = [1, 2, 3, 4, 5, 6, 7, 8, 9] # чисто лист с цифрами от 1 до 9
list_of_81filds = [i for i in range(1, 82)] # чисто лист с 81 номером ячеек
for i in range(9): # вывод на экран судоку
    for j in range(9):
        print(sudoku_fild[i][j], end=' ')
    print()        # конец вывода
buf_list_of9 = list_till9.copy()
for i in range(len(list_till9)):# заполняю рандомно первые 9 ячеек
    index_of_fild = random.choice(list_of_81filds) # рандомим ячейку
    del list_of_81filds[list_of_81filds.index(index_of_fild)]
    digit = random.choice(buf_list_of9) # рандомим цифру
    del buf_list_of9[buf_list_of9.index(digit)]
    print(index_of_fild, digit)
    sudoku_fild[index_of_fild // 9 if index_of_fild % 9 else (index_of_fild // 9) - 1][(index_of_fild % 9) - 1 if index_of_fild % 9 else 8] = digit
for i in range(9): # вывод на экран судоку
    for j in range(9):
        print(sudoku_fild[i][j], end=' ')
    print()        # конец вывода
