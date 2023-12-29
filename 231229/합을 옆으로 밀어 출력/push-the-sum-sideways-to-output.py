answer = ''
sum = 0
n = int(input())
for _ in range(n):
    sum += int(input())

sum = str(sum)
answer = sum[1:] + sum[:1]
print(answer)