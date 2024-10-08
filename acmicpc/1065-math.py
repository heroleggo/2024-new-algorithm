n = int(input())

cnt = 0

def check(i):
    if i < 100:
        return True
    else:
        data = str(i)
        for i in range(len(data) - 2):
            if int(data[i]) - int(data[i + 1]) != int(data[i + 1]) - int(data[i + 2]):
                return False
        return True

for i in range(1, n + 1):
    if check(i):
        cnt += 1

print(cnt)