input_string = input()
object_string = input()

if object_string not in input_string:
    print(-1)
else:
    for i in range(len(input_string) - len(object_string)):
        if input_string[i : i + len(object_string)] == object_string:
            print(i)
            break