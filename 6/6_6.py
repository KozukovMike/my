# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные
list_of_random_numbers = [int(i) for i in input()]
itog = list(filter(lambda x: not (x % 2), list_of_random_numbers)) + list(filter(lambda x: x % 2, list_of_random_numbers))
print(itog)
