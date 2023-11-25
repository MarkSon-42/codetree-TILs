n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    mul = 1
    while a != b:
        mul *= a
        a += 1
    print(mul * b)