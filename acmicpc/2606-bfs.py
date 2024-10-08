from collections import deque

n = int(input())
edges = int(input())

graph = [[0 for i in range(n)] for j in range(n)]

for i in range(edges):
    [s, e] = list(map(int, input().split()))
    graph[s - 1][e - 1] = 1
    graph[e - 1][s - 1] = 1

queue = deque()

queue.append(0)

visited = [0 for i in range(n)]

visited[0] = 1

while len(queue) != 0:
    v = queue.popleft()
    for i in range(n):
        if graph[v][i] == 1 and visited[i] == 0:
            visited[i] = 1
            queue.append(i)

cnt = 0

for i in range(n):
    if visited[i] == 1:
        cnt += 1
print(cnt - 1)