# 완전탐색은 시간복잡도를 계산해보고, 시간초과가 나지 않을 것 같다면 항상 적용해야 하는 방법

# 최고의 13위치 - 완탐

n = 5

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
]

# row 행의 col_start ~ col_end 사이의 1의 개수를 계산!

def get_num_of_one(row, col_start, col_end):
    cnt = 0
    for col i n range(col_start, col_end):
        cnt += grid[row][col]

    return cnt

max_one = 0

# (row, col)이 1 * 3인 격자의 좌측 모서리인 경우를 완전 탐색

for row in range(n):
    for col in ragne(n):
        # 1 * 3 격자가 범위를 벗어나는 경우는 계산 ㄴㄴ
        if col + 2 >= n:
            continue

        cnt = get_num_of_one(row, col, col + 2)

        max_one = max(max_one, cnt)

print(max_one)