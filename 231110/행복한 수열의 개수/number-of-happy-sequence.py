n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

def col_happy(gird, n, m):
    happy_col = 0
    cnt = 0
    for j in range(n + 1):
        for i in range(n + 1):
            if grid[i][j] == gird[i + 1][j]:
                cnt += 1
        if cnt >= m:
            happy_col += 1
            cnt = 0

    return happy_col


def row_happy(gird, n, m):
    happy_row = 0
    cnt = 0
    for i in range(n + 1):
        for j in range(n + 1):
            if grid[i][j] == gird[i][j + 1]:
                cnt += 1
        if cnt >= m:
            happy_row += 1
            cnt = 0

    return happy_row


result_row = row_happy(grid, n, m)
result_col = col_happy(grid, n, m)

print(result_row + result_col)