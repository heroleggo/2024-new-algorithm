n, k = tuple(map(int, input().split()))

data = [i + 1 for i in range(n)]

idx = 0

result = []

for i in range(n):
    idx += k - 1
    if idx >= len(data):
        idx = idx % len(data)
    result.append(str(data.pop(idx)))

print("<"+", ".join(result) + ">")