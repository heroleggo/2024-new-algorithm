n = int(input())

data = dict()

for i in range(n):
    name = input()
    if name in data:
        data[name] = data[name] + 1
    else:
        data[name] = 1

for i in range(n - 1):
    name = input()
    data[name] = data[name] - 1

for key, value in data.items():
    if value == 1:
        print(key)
        break