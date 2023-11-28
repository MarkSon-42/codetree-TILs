n = int(input())
str = list(input().split())

str = ''.join(str)

for i in range(len(str)//5 + 1):
    print(str[i * 5:(i + 1)*5])