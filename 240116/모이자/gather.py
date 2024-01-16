import sys

INT_MAX = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))
answer = INT_MAX
for i in range(n):
    min_val = 0
    for j in range(n):
        min_val += arr[j] * abs(i - j)

    answer = min(answer, min_val)

print(answer)