data = [0 for i in range(10010)]

calc = 0

def d(n):
    return n + sum(map(int, str(n)))

for i in range(1, 10000):
    calc = d(i)
    while calc <= 10000:
        data[calc] = 1
        calc = d(calc)

for i, v in enumerate(data):
    if v == 0 and 1 <= i <= 10000:
        print(i)