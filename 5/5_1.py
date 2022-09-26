# Вывести первые N цисел кратные M и больше K
N, M, K = int(input()), int(input()), int(input())
K += 1
while N > 0:
    if not (K % M):
        print(K)
        N -= 1
    K += 1
