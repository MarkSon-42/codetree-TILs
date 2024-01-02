n = int(input())
numbers_A = list(map(int, input().split()))
numbers_B = list(map(int, input().split()))

def check(numbers_A, numbers_B):
    for i in range(n):
        if numbers_A[i] not in numbers_B:
            return print('No')
    return print('Yes')
check(numbers_A, numbers_B)