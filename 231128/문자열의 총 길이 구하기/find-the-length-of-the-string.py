stringple = tuple(input().split())
answer = 0
for i in range(len(stringple)):
    answer += len(stringple[i])

print(answer)