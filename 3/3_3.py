a = [1,2, 3,4 ,5 ,6 ,7 ,8]
b = list(filter(lambda x: x%2, a))
c = list(filter(lambda x: not x%2, a))
print(b)
print(c)