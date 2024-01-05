# 변수 선언 및 입력:
n = int(input())
blocks = [int(input()) for _ in range(n)]

# 전체 블럭 수를 셉니다.
sum_of_blocks = sum(blocks)

avg = sum_of_blocks // n
ans = 0
for block_num in blocks:
    if block_num > avg:
        ans += block_num - avg

print(ans)