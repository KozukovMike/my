import random
import copy
def solve(board):

    def get_list_of_numbers(sudoku, ind_of_string, ind_of_colomn):
        """
        функция которая возвращает список элементов не доступных для данной ячейки
        :param sudoku: поле судоку
        :param ind_of_string: индекс строки данной ячейки
        :param ind_of_colomn: индекс стобца данной ячейки
        :return: список элементов недоступных для ячейки
        """
        set_of_free_digits = set()
        for j in range(9):
            set_of_free_digits.add(sudoku[ind_of_string][j])
        for i in range(9):
            set_of_free_digits.add(sudoku[i][ind_of_colomn])
        for i in range((ind_of_string // 3) * 3, ((ind_of_string // 3) + 1) * 3):
            for j in range((ind_of_colomn // 3) * 3, ((ind_of_colomn // 3) + 1) * 3):
                set_of_free_digits.add(sudoku[i][j])
        return list(set_of_free_digits)
    list_of_9 = [i for i in range(1, 10)]
    k = 0
    flag = False
    while k < 9:
        if k == 1:
            board1 = copy.deepcopy(board)
        if k == 2:
            board2 = copy.deepcopy(board)
        if k == 3:
            board3 = copy.deepcopy(board)
        if k == 4:
            board4 = copy.deepcopy(board)
        if k == 5:
            board5 = copy.deepcopy(board)
        if k == 6:
            board6 = copy.deepcopy(board)
        if k == 7:
            board7 = copy.deepcopy(board)
        for i in range(k + 1):
            if not board[i][k]:
                buf_list = list(set(list_of_9) - set(get_list_of_numbers(board, i, k)))
                print(buf_list)
                if not buf_list:
                    print(k, 'i')
                    flag = True
                    break
                board[i][k] = random.choice(buf_list)
        for j in range(k):
            if not board[k][j]:
                buf_list = list(set(list_of_9) - set(get_list_of_numbers(board, i, k)))
                print(buf_list)
                if not buf_list:
                    print(k, 'j')
                    flag = True
                    break
                board[k][j] = random.choice(buf_list)
        print('\n\n\n\n')
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=' ')
            print()
        if flag:
            flag = False
            if k == 2:
                board = copy.deepcopy(board1)
                k -= 2
            if k == 3:
                board = copy.deepcopy(board2)
                k -= 2
            if k == 4:
                board = copy.deepcopy(board2)
                k -= 3
            if k == 5:
                board = copy.deepcopy(board3)
                k -= 3
            if k == 6:
                board = copy.deepcopy(board4)
                k -= 3
            if k == 7:
                board = copy.deepcopy(board5)
                k -= 3
            if k == 8:
                board = copy.deepcopy(board6)
                k -= 3
            if k == 9:
                board = copy.deepcopy(board7)
                k -= 3
        k += 1
        print('\n\n\n\n')
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=' ')
            print()
solve([
            [9, 0, 0, 0, 8, 0, 0, 0, 1],
            [0, 0, 0, 4, 0, 6, 0, 0, 0],
            [0, 0, 5, 0, 7, 0, 3, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 4, 0],
            [4, 0, 1, 0, 6, 0, 5, 0, 8],
            [0, 9, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 7, 0, 3, 0, 2, 0, 0],
            [0, 0, 0, 7, 0, 5, 0, 0, 0],
            [1, 0, 0, 0, 4, 0, 0, 0, 7]
        ])
