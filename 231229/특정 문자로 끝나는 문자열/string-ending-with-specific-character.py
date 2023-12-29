string_list = []
for _ in range(10):
    string = input()
    string_list.append(string)

last_char = input()

answer = []
flag = 0

# print(string_list, last_char)
for c in string_list:
    if c[-1] == last_char:
        flag = 1
        answer.append(c)

if flag == 1:
    for x in answer:
        print(x)
else:
    print('None')