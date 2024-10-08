from collections import deque

[m, n] = list(map(int, input().split()))

data = []

def check(x, y, row, col):
    return 0 <= x < row and 0 <= y < col

for i in range(n):
    data.append(list(map(int, input().split())))

queue = deque()
cnt = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            queue.append([i, j])

while len(queue) != 0:
    cnt += 1
    tmp = []
    while len(queue) != 0:
        [x, y] = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(nx, ny, n, m) and data[nx][ny] == 0:
                tmp.append([nx, ny])
                data[nx][ny] = 1
    for pos in tmp:
        queue.append(pos)

result = cnt - 1

for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            result = -1

print(result)