# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int
n = int(input())
def is_bin(st: str) -> bool:
    return st[1] == 'b'
print(is_bin('0b001'))
def number_system(n):
    if n in [0, 1]:
        return str(n)
    else:
        return str(n % 2) + number_system(n // 2)
print(number_system(n)[::-1])
