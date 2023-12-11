# 마지막으로 방문한 위치

# 이동한 경로 상의 숫자 합

# 마지막으로 방문한 위치가 같다면, 이동한 경로 상의 숫자 합은 클수록 더 좋다.

# dp[i][j]에 대한 정의 " 마지막으로 방문한 위치 (i, j)라 했을 떄, 얻을 수 있는 최대 합"

# dp[i][j] = max(dp[i-1][j] + a[i][j], max(dp[i-1][dp]))

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        dp[i][j] = max(dp[i - 1][j] + arr[i][j], dp[i][j + 1] + arr[i][j])

print(dp[n - 1][0])