n = int(input())

dp = [-1 for i in range(5000)]

# 3th value
dp[2] = 1

# 5th value
dp[4] = 1
for i in range(5, n):
    if dp[i - 3] != -1 or dp[i - 5] != -1:
        if dp[i - 3] != -1:
            if dp[i - 5] != -1:
                dp[i] = min(dp[i - 3], dp[i - 5]) + 1
            else:
                dp[i] = dp[i - 3] + 1
        if dp[i - 5] != -1:
            dp[i] = dp[i - 5] + 1

print(dp[n - 1])