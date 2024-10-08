[n, m] = list(map(int, input().split()))

data = [i + 1 for i in range(n)]

def print_data(arr):
    print(' '.join(map(str, arr)))

def permutation(k):
    def choose(chosen):
        if len(chosen) == k:
            print_data(chosen)
            return
        for i in data:
            if i not in chosen:
                chosen.append(i)
                choose(chosen)
                chosen.pop()

    choose([])

permutation(m)