def count_ways_to_fill_square(n):
    if n <= 2:
        return n

    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 3

    for i in range(3, n + 1):
        ways[i] = (ways[i - 1] + ways[i - 2] * 2) % 10007

    return ways[n]

# Read input
n = int(input())

# Output the number of ways modulo 10,007
result = count_ways_to_fill_square(n)
print(result)