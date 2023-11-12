def one_to_nine_rect(number):
    num = 1
    for i in range(number):
        for j in range(number):
            if num > 9:
                num = 1
                print(num, end=' ')
            else:
                print(num, end=' ')
            num += 1
        print()


n = int(input())
one_to_nine_rect(n)