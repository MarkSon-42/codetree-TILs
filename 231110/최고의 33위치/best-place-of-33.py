n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 행 시작 열 시작 ~ 행 끝, 열 끝 사이의 금의 개수를 계산

def get_num_of_gold(row_start, col_start, row_end, col_end):
    gold = 0

    for row in range(row_start, row_end + 1):
        for col in range(col_start, col_end + 1):
            gold += grid[row][col]

    return gold

max_gold = 0

for row in range(n):
    for col in range(n):
        if row + 2 >= n or col + 2 >= n:
            continue
        num_of_gold = get_num_of_gold(row, col, row + 2, col + 2)

        max_gold = max(max_gold, num_of_gold)

print(max_gold)