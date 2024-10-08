import math

def check(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

[m, n] = list(map(int, input().split()))

for i in range(m, n + 1):
    if check(i):
        print(i)