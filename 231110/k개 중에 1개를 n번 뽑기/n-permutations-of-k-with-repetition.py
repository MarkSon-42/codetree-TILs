k, n = map(int, input().split())

answer = []

def print_result():
    for elem in answer:
        print(elem, end=' ')
    print()

def dfs():

    if len(answer) == n:
        print_result()
        return

    for i in range(1, k + 1):
        answer.append(i)
        dfs()
        answer.pop()
    return
    

dfs()