input_string = input()
object_string = input()

if input_string == object_string:
    print(0)

elif object_string not in input_string:
    print(-1)
else:

    for i in range(len(input_string) - len(object_string) + 1):

        if input_string[i : i + len(object_string)] == object_string:
            print(i)
            break