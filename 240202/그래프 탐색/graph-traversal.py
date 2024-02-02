# 그래프 탐색 알고리즘의 2가지 대원칙을 꼭 기억하셔야 합니다.

# 시작점으로부터 연결된 모든 정점을 전부 방문해야 합니다.
# 이미 방문한 정점은 다시는 방문하지 않습니다.
# 만약 이미 방문한 정점을 다시 방문할 수 있도록 한다면, 1번 정점에서 시작하여 2번 정점으로 갔다가, 다시 2번 정점은 1번 정점과 연결되어 있으므로 1번 정점으로 오며 1, 2를 계속 왔다갔다 하는 것을 반복하게 될 것입니다.

# 따라서 다음과 같이 정점의 개수만큼의 크기를 갖는 visited 배열을 만들어 그 다음 DFS 함수를 호출하기 전에 꼭 해당 위치의 visited 값을 true로 변경하여, 다시는 탐색 도중에 해당 위치에 방문하지 않도록 해야만 합니다.

import sys
from collections import defaultdict

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
visited = [False] * (N + 1)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1)

print(visited.count(True) - 1)