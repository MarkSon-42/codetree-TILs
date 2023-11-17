# dir_num = 2
# x, y = 1, 5
# dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

# nx, ny = x + dx[dir_num], y + dy[dir_num]


n = int(input())

x, y = 0, 0

for i in range(n):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    dir, dist = tuple(input().split())
    dist = int(dist)

    if dir == "E":
        move_dir = 0
    if dir == "S":
        move_dir = 1
    if dir == "W":
        move_dir = 2
    if dir == "N":
        move_dir = 3

    x = x + dx[move_dir] * dist
    y = y + dy[move_dir] * dist

print(x, y)