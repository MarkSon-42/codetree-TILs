# 이렇듯 현재 풀려고 하는 문제가 복잡하다면, 크게 생각하여 이미 해당 함수가 주어져있다고 가정하고 코드를 작성한 뒤, 이후에 실제 필요했던 함수를 작성해내는 식으로 진행하는 것이 좋습니다.# 두 자리 숫자 중 3의 배수는 아니면서 십의 자리 숫자와 일의 자리 숫자가 다른 수의 개수를 세는 프로그램



def is_magic_number(n):
    return n % 3 != 0 and all_different(n)

def all_different(n):
    return (n // 10) != (n % 10) 


cnt = 0
for i in range(10, 100):
    if is_magic_number(i):
        cnt += 1
print(cnt)

#
# is_magic_number를 어떻게 작성할지..
# 핵심은 우선 저렇게 함수를 호출부터 하고
# 구현해보기..