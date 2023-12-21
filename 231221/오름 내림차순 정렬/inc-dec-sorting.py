n = int(input())
arr = list(map(int, input().split()))

asending = sorted(arr)
desending = sorted(arr, reverse = True)

for num in asending:
    print(num, end = ' ')


for num in desending:
    print(num, end = ' ')