a = list(input().split())
b = list(input().split())

a = a.sort()
b = b.sort()

if a == b:
    print("Yes")
else:
    print("No")