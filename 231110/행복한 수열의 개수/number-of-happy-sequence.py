n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

seq = [0 for _ in range(n)]

def is_happy_seq():
    consec_count, max_count = 1, 1
    for i in range(1, n):
        if seq[i - 1] == seq[i]:
            consec_count += 1  # 연속 카운트
        else:
            consec_count = 1  # 연속이 깨지면 1로 갱신

        max_count = max(consec_count, max_count)

    # 최대로 연속한 회수가 m이상이면 true반환
    return max_count >= m



num_happy = 0


# 가로로 행복한 수열의 수 세기
for i in range(n):
    seq = grid[i][:]

    if is_happy_seq():
        num_happy += 1

# 세로

for j in range(n):
    #  ! : 세로로 숫자들을 모아 새로운 수열을 만들기  -> 세로 요소를 가로로 재배치해서 수열 행태로
    # 그래야 is_happy_seq()의 파라미터에 맞출 수 있음!
    for i in range(n):
        seq[i] = grid[i][j]

    if is_happy_seq():
        num_happy += 1

print(num_happy)