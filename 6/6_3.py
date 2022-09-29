# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]
N = int(input())
our_lst = [int(i) for i in input()]
def shift(n: int, l: list) -> list:
    res_lst = []
    for i in range(len(l)):
        res_lst.append(l[(i + n + 1) % len(l)])
    return res_lst
print(shift(N, our_lst))
