c = []
n = int(input())
for _ in range(n):
    c.append(input())

c.sort()
for char in c:
    print(char)