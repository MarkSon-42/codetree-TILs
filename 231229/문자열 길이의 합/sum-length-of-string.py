total = 0
cnt_a = 0
n = int(input())
for _ in range(n):
    string = input()
    total += len(string)
    if string[0] == 'a':
        cnt_a += 1

print(total, cnt_a)