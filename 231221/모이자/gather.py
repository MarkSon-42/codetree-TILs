n = int(input())
home = list(map(int, input().split()))
min_val = 1000000
dist_sum = 0
for i in range(len(home)):
    for j in range(len(home)):
        dist_sum += (abs(i - j)) * home[j]
    if dist_sum < min_val:
        min_val = dist_sum
    
    dist_sum = 0

print(min_val)