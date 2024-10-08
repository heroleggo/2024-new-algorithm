from collections import deque

[n, m] = list(map(int, input().split()))

maze = []

for i in range(n):
    maze.append(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

queue = deque()

queue.append([0, 0])

visited = [[0 for i in range(m)] for j in range(n)]

visited[0][0] = 1

while len(queue) != 0:
    [x, y] = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '1':
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])
            elif visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])

print(visited[n - 1][m - 1])