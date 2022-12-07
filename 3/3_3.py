a = [1, 2, 3]
def ss(b):
    c = []
    for i in range(3):
        a[i] += 10
    return c

k = ss(a)
print(a)