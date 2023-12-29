answer = []
string = input()
first = string[:1]
second = string[1:2]

for c in string:
    if c == first:
        answer.append(second)
    elif c == second:
        answer.append(first)
    else:
        answer.append(c)

print(''.join(answer))