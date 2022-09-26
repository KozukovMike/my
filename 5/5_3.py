# **Вывести четные числа от 2 до N по 5 в строку
n = int(input())
for i in range(2, n, 2):
    print(i, end=' ')
    if not (i % 10):
        print()
