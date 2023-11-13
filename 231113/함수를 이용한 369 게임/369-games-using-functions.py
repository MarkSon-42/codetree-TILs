tsn = ['3', '6', '9']
def is_threesixnine(n):
    n = str(n)
    for i in range(len(n)):
        if n[i] in tsn:
            return True
    return False

a, b = map(int, input().split())
cnt = 0
for i in range(a, b + 1):
    if i % 3 == 0 or is_threesixnine(i):
        cnt += 1

print(cnt)