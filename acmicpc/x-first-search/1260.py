from collections import deque

[n, m, v] = list(map(int, input().split()))

data = [[0 for i in range(n)] for j in range(n)]

for i in range(m):
    [s, e] = list(map(int, input().split()))
    data[s - 1][e - 1] = 1
    data[e - 1][s - 1] = 1

def bfs(graph, start):
    visited = [0 for i in range(n + 1)]
    order = [start]
    queue = deque()

    visited[start] = 1
    queue.append(start)

    while len(queue) != 0:
        v = queue.popleft()
        for i in range(n):
            if data[v - 1][i] == 1 and visited[i + 1] == 0:
                visited[i + 1] = 1
                order.append(i + 1)
                queue.append(i + 1)

    return order

visit = [0 for i in range(n + 1)]
o = []

def dfs(graph, start):
    visit[start] = 1
    o.append(start)

    for i in range(n):
        if data[start - 1][i] == 1 and visit[i + 1] == 0:
            dfs(graph, i + 1)

dfs(data, v)
print(' '.join([str(x) for x in o]))
print(' '.join([str(x) for x in bfs(data, v)]))