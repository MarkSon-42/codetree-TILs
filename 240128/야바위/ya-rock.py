n = int(input())
a, b, c = [list(map(int, input().split())) for _ in range(n)]

max_score = 0

# Assume all starting positions
# Calculate the maximum score among them
for i in range(1, 4):
    # Empty all paper cups: initialization
    yabawi = [0, 0, 0, 0]

    yabawi[i] = 1

    score = 0

    for j in range(n):
        a, b, c = abc[j]
        yabawi[a], yabawi[b] = yabawi[b], yabawi[a]

        if yabawi[c]:
            score += 1

    max_score = max(max_score, score)

print(max_score)