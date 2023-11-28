fr = ["apple", "banana", "grape", "blueberry", "orange"]
answer = []
ch = input()
cnt = 0
for i in range(len(fr)):
    for j in range(len(fr[i])):
        if fr[i][2] == ch:
            cnt += 1
            answer.append(fr[i])
            break
        if fr[i][3] == ch:
            cnt += 1
            answer.append(fr[i])
            break

answer = list(set(answer))
for i in range(len(answer)):
    print(answer[i])
print(cnt)