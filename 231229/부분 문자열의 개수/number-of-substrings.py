input_string = input()
object_string = input()
cnt = 0
for i in range(len(input_string) - len(object_string) + 1):
    if input_string[i : i + len(object_string)] == object_string:
        cnt += 1

print(cnt)