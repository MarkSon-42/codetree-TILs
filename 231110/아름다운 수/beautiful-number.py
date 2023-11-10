# 호출 상태 
# 종료 조건 
# 호출 함수 내부 작성 

n= int(input()) #n 자릿수의 아름다운 수 
cnt = 0  #아름다운 수의 개수 
answer = [ 0 for _ in range(n)] # 아름다운 수 자체를 출력할필요없어서 필요없는 구문 인듯 

def func(idx): # 0 ~ (idx-1) 까지는 아름다운 수를 채웠다.
               # idx ~ (n-1) 자리 까지 아름다운수를 채울 예정이다.
    #종료조건 
    if idx == n : # 0~ n-1 까지 아름다운 수를 채웠다면 끝     ##############여기에서 n을 불러올땐 그냥 불러왔는데 
        global cnt ###########################여기에 굳이 global cnt 를 불러오는 이유를 잘 모르겠습니다. 
        cnt +=1
        return
    
    #재귀 호출 내부 
    #숫자를 추가한다.
    for num in range(1,5) : # 1부터 4까지의 수를 해당 개수만큼 추가하겠다

        if idx +num > n: #이부분에 idx+num > n 을 써야 답이 나오는게 잘이해가 안감.. 

            break

        #for i in range(num):   # 출력할필요가 없는 부분이라.. 이거 적을필요가 없음.. 
        #    answer[idx+i] = num  #값 추가 

        func(idx+num)

func(0) # 아름다운수 찾기 시작.. 함수 호출 해야함.. 
print(cnt)