# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int
inp = input()
which_number_system = int(input())
def number_system(s: str, a: int):
    if a == 2:
        s = int(s)
        res = ''
        while s not in [0, 1]:
            res += str(s % 2)
            s //= 2
        res += str(s)
        return res[::-1]
    elif a == 10:
        res = 0
        for i in range(len(s)):
            res += int(s[i]) * 2**(len(s) - (i + 1))
        return res
print(number_system(inp, which_number_system))
