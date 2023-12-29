string_list = []
for _ in range(10):
    string = input()
    string_list.append(string)

last_char = input()

answer = []

# print(string_list, last_char)
for c in string_list:
    if c[-1] == last_char:
        answer.append(c)
for x in answer:
    print(x)