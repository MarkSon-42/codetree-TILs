cnt = 1
answer = []
string = input()

for i in range(len(string) - 1):
    if string[i] == string[i + 1]:
        cnt += 1
        if i == len(string) - 2:
            answer.append(string[i])
            answer.append(str(cnt))
            break
        continue
    else:
        if i == len(string) - 1:
            answer.append(string[i])
            answer.append('1')
            break
        answer.append(string[i])
        answer.append(str(cnt))
        cnt = 1

print(len(answer))
print(''.join(answer))