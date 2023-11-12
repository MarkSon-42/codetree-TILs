def lcm(x, y):
    
    def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

    result = (x * y) // gcd(x, y)
    print(result)

n, m = map(int, input().split())
lcm(n, m)