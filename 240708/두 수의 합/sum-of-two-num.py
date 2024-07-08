n,k = map(int,input().split())
arr = list(map(int, input().split()))

numb = dict()
cnt = 0

for i in range(n):
    # 현재 값과 짝꿍이 될 수 있는 값을 말한다.
    diff = k - arr[i] 
    
    # 짝꿍이 될 수 있는 값이 이미 딕셔너리에 추가되어 있다면 
    # 현재 값과 짝꿍이 될 후보가 그 수만큼 있다는 뜻이다.
    # 즉 그 수만큼 경우의 수가 증가하면 된다.
    if diff in numb:  
        cnt += numb[diff]
    
    # 현재 값은 다른 숫자들의 짝꿍 후보가 될 수 있기에
    # 딕셔너리에 현재 값을 넣어준다.
    # 이미 같은 값이 존재한다면 개수를 늘려주면 된다.
    if arr[i] in numb:
        numb[arr[i]] += 1
    else:
        numb[arr[i]] = 1

# 마지막 경우의 수를 출력한다.
print(cnt)
출처: https://code-angie.tistory.com/127 [CodeAngie:티스토리]