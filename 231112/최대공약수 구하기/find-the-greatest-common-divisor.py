def gcd(x, y):
   while y:
       x, y = y, x % y
   print(x)
n, m = map(int, input().split())
gcd(n, m)