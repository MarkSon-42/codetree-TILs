from collections import deque


def bfs(n, m, maze):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = 0  # 이렇게 하면 굳이 visited를 따로 선언할 필요가 없음

                queue.append((nx, ny))

                if nx == n - 1 and ny == m - 1:
                    return True
    return False


n, m = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(n)]

answer = bfs(n, m, maze)

print(1 if answer else 0)