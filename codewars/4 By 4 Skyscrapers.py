
def solve_puzzle(clues):
    res = [[0 for i in range(6)] for j in range(6)]
    clues = [[clues[i + j*4] for i in range(4)] for j in range(4)]
    print(clues)
    for j in range(1, 5):
        res[0][j] = clues[0][j - 1]
        if res[0][j] == 1:
            res[1][j] = 4
        if res[0][j] == 4:
            for i in range(1, 5):
                res[i][j] = i
    for j in range(1, 5):
        res[j][5] = clues[1][j - 1]
        if res[j][5] == 1:
            res[j][4] = 4
        if res[j][5] == 4:
            for i in range(1, 5):
                res[j][i] = 5 - i
    for j in range(4, 0, -1):
        res[5][j] = clues[2][4 - j]
        if res[5][j] == 1:
            res[4][j] = 4
        if res[5][j] == 4:
            for i in range(1, 5):
                res[i][j] = 5 - i
    for j in range(4, 0, -1):
        res[j][0] = clues[3][4 - j]
        if res[j][0] == 1:
            res[j][1] = 4
        if res[j][0] == 4:
            for i in range(1, 5):
                res[j][i] = i


    def vivod(field):
        for i in field:
            for j in i:
                print(j, end=' ')
            print()


    vivod(res)


    def find_possible(field, ind_i, ind_j):
        buf = []
        for i in range(1, 5):
            buf.append(field[i][ind_j])
        for j in range(1, 5):
            buf.append(field[ind_i][j])
        if ind_i == 1:
            if field[ind_i - 1][ind_j] == 2:
                buf.append(4)
            if field[ind_i - 1][ind_j] == 3:
                buf += [3, 4]
        if ind_i == 4:
            if field[ind_i + 1][ind_j] == 2:
                buf.append(4)
            if field[ind_i + 1][ind_j] == 3:
                buf += [3, 4]
        if ind_j == 1:
            if field[ind_i][ind_j - 1] == 2:
                buf.append(4)
            if field[ind_i][ind_j - 1] == 3:
                buf += [3, 4]
        if ind_j == 4:
            if field[ind_i][ind_j + 1] == 2:
                buf.append(4)
            if field[ind_i][ind_j + 1] == 3:
                buf += [3, 4]
        return list(set([1, 2, 3, 4]) - set(buf))
    for i in range(1, len(res) - 1):
        list_of_lists_inarow = []
        for j in range(1, len(res) - 1):
            if not res[i][j]:
                buf = find_possible(res, i, j)
                print(buf, [i, j], end=' ')
                if len(buf) == 1:
                    res[i][j] = buf[0]
    print()
    vivod(res)
solve_puzzle((0, 0, 1, 2, 0, 2, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0))

