# def print_rect(n, m):
#     for _ in range(n):
#         print("*" * m)


# row_num, col_num = tuple(map(int, input().split()))
# print_rect(row_num, col_num)

# >> 3 5

# *****
# *****
# *****


def print_squarestarts(n, m):
    for _ in range(n):
        print("1" * m)

n, m = map(int, input().split())
print_squarestarts(n, m)