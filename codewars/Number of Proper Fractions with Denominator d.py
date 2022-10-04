def proper_fractions(n):
    lst = []
    count = 0
    for i in range(2, n // 2):
        if not (n % i):
            lst.append(i)
    for i in range(1, n):
        count2 = 0
        for j in lst:
            if i % j:
                count2 += 1
            else:
                break
        if count2 == len(lst):
            count += 1
    return count
number = int(input())
print(proper_fractions(number))
