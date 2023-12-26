import sys

INT_MIN = -sys.maxsize

n = 5
dp = [0] * n
a = [2, 3, 0, 1, 4]

def init():
    for i in range(n):
        dp[i] = INT_MIN

    dp[0] = 0

init()

for i in range(1, n):
    for j in range(0, i):
        if dp[j] == INT_MIN:
            continue

        if j + a[j] >= i:
            dp[i] = max(dp[i], dp[j] + 1)

answer = 0
for i in range(n):
    answer = max(answer, dp[i])

print(answer)