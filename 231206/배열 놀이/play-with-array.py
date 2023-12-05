n, q = map(int, input().split())

elems = [0] + list(map(int, input().split()))

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        print(query[1])
    elif query[0] == 2:
        if query[1] in elems:
            print(elems.index(query[1]))
        else:
            print(0)
    elif query[0] == 3:
        a, b = query[1], query[2]
        for j in range(a, b + 1):
            print(elems[j], end = ' ')