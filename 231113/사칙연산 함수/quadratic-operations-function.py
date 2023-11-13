# 변수 선언 및 입력:
a, o, c = input().split()
a = int(a)
c = int(c)

# 두 수의 합을 반환하는 함수를 작성합니다.
def plus(a, b):
    return a + b

# a에서 b를 뺀 값을 반환하는 함수를 작성합니다.
def minus(a, b):
    return a - b

# 두 수의 곱을 반환하는 함수를 작성합니다.
def times(a, b):
    return a * b

# a를 b로 나눈 나머지를 반환하는 함수를 작성합니다.
def divide(a, b):
    return a // b


if o == '+':
    print(a, "+", c, "=", plus(a, c))
elif o == '-':
    print(a, "-", c, "=", minus(a, c))
elif o == '*':
    print(a, "*", c, "=", times(a, c))
elif o == '/':
    print(a, "/", c, "=", divide(a, c))
else:
    print("False")