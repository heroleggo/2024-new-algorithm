n = int(input())

dp = [0 for i in range(10 ** 6 + 1)]

# 1 -> 0
dp[1] = 0
# 2 -> 1
dp[2] = 1
# 3 -> 1
dp[3] = 1

for i in range(4, n + 1):
    if i % 6 == 0:
        dp[i] = min(dp[i // 3], dp[i // 2], dp[i - 1]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i // 2], dp[i - 1]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i // 3], dp[i - 1]) + 1
    else:
        dp[i] = dp[i - 1] + 1

print(dp[n])