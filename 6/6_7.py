# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

list_of_numbers = [int(i) for i in input()]
def sum_of_neighbors(lst):
    res = []
    for i in range(len(lst)):
        res.append(lst[(i - 1) % len(lst)] + lst[(i + 1) % len(lst)])
    return res
print(sum_of_neighbors(list_of_numbers))
