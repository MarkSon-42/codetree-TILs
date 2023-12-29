string = input()
reversed_string = string[::-1]

for i in range(len(reversed_string)):
    if i % 2 == 0:
        print(reversed_string[i], end='')