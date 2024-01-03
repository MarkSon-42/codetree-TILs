n, k, t = map(str, input().split())
n, k = int(n), int(k)

string = [input() for _ in range(n)]
answer = []
for c in string:
    if c[:len(t)] == t:
        answer.append(c)

answer = sorted(answer)

print(answer[k - 1])