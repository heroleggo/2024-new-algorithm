n = int(input())

data = list(map(int, input().split()))

result = 0

data.sort()

for i in range(1, n + 1):
    result += sum(data[0:i])

print(result)