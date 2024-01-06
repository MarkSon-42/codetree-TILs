# 변수 선언 및 입력:
x1, x2, x3, x4 = tuple(map(int, input().split()))


def intersecting(x1, x2, x3, x4):
    # 겹치지 않는 경우에 대한 처리를 먼저 진행합니다.
    if x2 < x3 or x4 < x1:
        return False
    # 나머지는 전부 겹치는 경우라고 볼 수 있습니다.
    else:
        return True


# 겹치는지를 확인합니다.
if intersecting(x1, x2, x3, x4):
    print("intersecting")
else:
    print("nonintersecting")