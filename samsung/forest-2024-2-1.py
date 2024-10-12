from collections import deque

[R, C, K] = list(map(int, input().split()))

elf_list = []

# 판 위에 입장 대기중인 골렘이 서있다고 생각하기
board = [[0 for _ in range(C)] for _ in range(R + 3)]
is_exit = [[0 for _ in range(C)] for _ in range(R + 3)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0

for _ in range(K):
    [col, direction] = list(map(int, input().split()))
    elf_list.append((col - 1, direction))

# r, c 기준의 골렘이 숲 안에 위치하는지 체크 (윗방향으로는 일단 미체크, 아랫방향 및 좌우 체크)
def in_forest(r, c):
    return 3 <= r < R + 3 and 0 <= c < C

# r, c 중심점을 기준으로 이동이 가능한지 체크
# d 방향 1 -> 오른쪽 아래, 2 -> 바로 아래, 3 -> 왼쪽 아래, 0인 U는 불가능함 골렘 이동로직상
#
def can_move(r, c):
    # r, c 기준 골렘이랑 r - 1, c 기준 골렘 위치 전부 체크
    # 그래야 해당 위치로 이동할 수 있음 (좌 -> 하, 우 -> 하, 즉하)
    return (c - 1 >= 0 and c + 1 < C and r + 1 < R + 3 and board[r][c] == 0 and board[r - 1][c] == 0 and board[r + 1][c] == 0
        and board[r][c - 1] == 0 and board[r - 1][c - 1] == 0 and board[r][c + 1] == 0 and board[r - 1][c + 1] == 0)

def reset():
    global board, is_exit
    for i in range(R + 3):
        for j in range(C):
            board[i][j] = 0
            is_exit[i][j] = 0

def move(r, c, d, idx):
    global board, is_exit
    # 아래로 움직이기
    if can_move(r + 1, c):
        move(r + 1, c, d, idx)
    # 왼쪽 아래로 움직이기 (출구 방향을 반시계로)
    elif can_move(r + 1, c - 1):
        move(r + 1, c - 1, (d + 3) % 4, idx)
    # 오른쪽 아래로 움직이기 (출구 방향을 시계로)
    elif can_move(r + 1, c + 1):
        move(r + 1, c + 1, (d + 1) % 4, idx)
    # 모든 방향으로 못움직일 경우
    else:
        # 몸의 일부가 빠져나가 있는지 체크
        if not in_forest(r - 1, c - 1) or not in_forest(r + 1, c + 1):
            # 몸의 일부가 숲을 벗어남
            reset()
        else:
            # 그 자리에 골렘 위치
            board[r][c] = idx
            for i in range(4):
                board[r + dx[i]][c + dy[i]] = idx
            # 출구 기록
            is_exit[r + dx[d]][c + dy[d]] = 1

            global answer
            # 현재 숲을 기준으로 BFS 탐색 통해 최대 행번호 추출 (2를 빼야 실제 행번호, 첫 데이터 선언 시 R + 3, 인덱스 0부터 시작 -> 1로)
            answer += bfs((r, c)) - 2
    return

def bfs(pos):
    x, y = pos
    res = x
    visited = [[0 for _ in range(C)] for _ in range(R + 3)]
    queue = deque()
    queue.append(pos)
    visited[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if in_forest(nx, ny) and visited[nx][ny] == 0 and (board[cx][cy] == board[nx][ny] or (board[nx][ny] != 0 and is_exit[cx][cy] == 1)):
                visited[nx][ny] = 1
                queue.append((nx, ny))
                res = max(res, nx)
    return res

def print_arr(arr):
    for i in arr:
        print(i)

for k in range(K):
    col, d = elf_list[k]
    move(0, col, d, k + 1)

print(answer)