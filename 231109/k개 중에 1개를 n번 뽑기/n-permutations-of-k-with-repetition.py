# for i in range(1, n + 1):
#     if visited[i]:
#         continue
#

k, n = map(int, input().split())
s = []

def dfs():
    if len(s) == n:
        print(' '.join(map(str, s)))
        return

    for i in range(1, k + 1):
        s.append(i)
        dfs()
        s.pop()


dfs()