n, m = map(int, input().split())
coins = list(map(int, input().split()))


dp = [m + 1] * (m + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, m + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[m] if dp[m] != m + 1 else -1)