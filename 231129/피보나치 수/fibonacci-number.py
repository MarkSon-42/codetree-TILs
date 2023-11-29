p = [0] * 46

p[1] = 1
p[2] = 1

n = int(input())

for i in range(3, n):
    if n >= 3:
        p[n] = p[n-2] + p[n-1] 
    else:
        print(p[n])
        break

print(p[n])