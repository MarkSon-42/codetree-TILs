n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

def type_a(x, y, arr):
    can_sum = []
    for i in range(x + 1):
        for j in range(y + 1):
            # type a = grid[i][j] + grid[i+1][j] + grid[i+1][j+1]
            if i + 1 > x or j + 1 > y:
                continue
            else:
                can_sum.append(arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1])
    return max(can_sum)
def type_b(x, y, arr):
    can_sum = []
    for i in range(x + 1):
        for j in range(y + 1):
            # type a = grid[i][j] + grid[i+1][j] + grid[i+1][j+1]
            if j + 2 > y:
                continue
            else:
                can_sum.append(arr[i][j] + arr[i][j + 1] + arr[i][j + 2])
    return max(can_sum)

print(max(type_a(n, m, grid), type_b(n, m, grid)))