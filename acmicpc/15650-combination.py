[n, m] = list(map(int, input().split()))

data = [i + 1 for i in range(n)]

def print_data(arr):
    print(' '.join(map(str, arr)))

def combination(k, idx = 0, arr = []):
    if len(arr) == k:
        print_data(arr)
        return
    if idx >= len(data):
        return

    combination(k, idx + 1, arr + [data[idx]])

    combination(k, idx + 1, arr)

combination(m)