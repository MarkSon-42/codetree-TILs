def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a, b = map(int, input().split())

_sum = 0
for i in range(a, b + 1):

    if i == 1:
        continue
    if is_prime(i):
        _sum += i

print(_sum)