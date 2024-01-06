x1, x2, x3, x4 = map(int, input().split())



if x1 <= x2 or x2 >= x3 or x4 <= x3: 
    print("intersecting")
else:
    print("nonintersetting")