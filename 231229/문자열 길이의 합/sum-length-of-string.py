total = 0
cnt_a = 0
n = int(input())
for _ in range(n):
    string = input()
    total += len(string)
    cnt = string.count('a')
    cnt_a += cnt

print(total, cnt_a)