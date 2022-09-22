a, b, c = float(input()), float(input()), float(input())
positive = str(int(a > 0) + int(b > 0) + int(c > 0))
negative = str(int(a < 0) + int(b < 0) + int(c < 0))
print('positive:' + positive, 'negative:' + negative)

