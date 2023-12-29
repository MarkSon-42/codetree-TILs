string = input()
length = len(string)
answer = string[:1] + 'a' + string[2:length - 2] + 'a' + string[-1]
print(answer)