n = int(input())

cnt = 0

placed = [0 for i in range(n)]

check = [False for j in range(n)]

def intersect(row):
    for i in range(row):
        if placed[i] == placed[row] or row - i == abs(placed[i] - placed[row]):
            return True
    return False

def queen(row= 0):
    global cnt
    if row == n:
        cnt += 1
        return
    for i in range(n):
        if check[i]:
            continue
        placed[row] = i
        if not intersect(row):
            check[i] = True
            queen(row + 1)
            check[i] = False

queen()

print(cnt)